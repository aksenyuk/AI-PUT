#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('labrob_detector')
import sys
import rospy
import cv2

import numpy as np
import time
import os

from sensor_msgs.msg import CompressedImage, Image  # 1 : import proper Image message

from cv_bridge import CvBridge, CvBridgeError

import rospkg

from vision_msgs.msg import Detection2DArray, Detection2D, ObjectHypothesisWithPose, BoundingBox2D  # 3: Import proper ROS detection messages
from geometry_msgs.msg import PoseWithCovariance, Pose2D, Pose, Point 


class image_converter:
	def __init__(self):	
		print('Initializing...')

		# 1: input image subscriber
		self.subscriber_image = rospy.Subscriber(
			'/camera/raw_image/compressed',
			CompressedImage, self.callback)

		# 2: Add image publisher
		self.publisher_image = rospy.Publisher(
			'image_converter/converted_image',
			Image, queue_size=10)

		# 3: Add 2D detections publisher
		self.publisher_detection = rospy.Publisher(
			'image_converter/detection2D',
			Detection2DArray, queue_size=10)

		self.bridge = CvBridge()
		self.i = 0
		print('Initialized image converter')

	def callback(self,data):
		print('\tconverting image ' + str(self.i))
		self.i += 1
		try:
			image = self.bridge.compressed_imgmsg_to_cv2(data)  # 1: Add code that converts ROS image to OpenCV image.
		except CvBridgeError as e:
			print(e)

		rospack = rospkg.RosPack()
		package_path = rospack.get_path('labrob_detector')

		# load the COCO class labels our YOLO model was trained on
		# 1: What path is used here?
		# 		*/labrob_detector/yolo-coco/coco.names
		labelsPath = os.path.sep.join([package_path, "yolo-coco", "coco.names"])
		LABELS = open(labelsPath).read().strip().split("\n")

		# initialize a list of colors to represent each possible class label
		np.random.seed(42)
		COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

		# derive the paths to the YOLO weights and model configuration
		weightsPath = os.path.sep.join([package_path, "yolo-coco", "yolov3.weights"])
		configPath = os.path.sep.join([package_path, "yolo-coco", "yolov3.cfg"])

		# load our YOLO object detector trained on COCO dataset (80 classes)
		#print("[INFO] loading YOLO from disk...")
		net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

		# load our input image and grab its spatial dimensions
		(H, W) = image.shape[:2]

		# determine only the *output* layer names that we need from YOLO
		ln = net.getLayerNames()
		ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

		# construct a blob from the input image and then perform a forward
		# pass of the YOLO object detector, giving us our bounding boxes and
		# associated probabilities
		blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
		net.setInput(blob)
		start = time.time()
		layerOutputs = net.forward(ln)
		end = time.time()

		# show timing information on YOLO
		#print("[INFO] YOLO took {:.6f} seconds".format(end - start))

		# initialize our lists of detected bounding boxes, confidences, and
		# class IDs, respectively
		boxes = []
		confidences = []
		classIDs = []

		# loop over each of the layer outputs
		for output in layerOutputs:
			# loop over each of the detections
			for detection in output:
				# extract the class ID and confidence (i.e., probability) of
				# the current object detection
				scores = detection[5:]
				classID = np.argmax(scores)
				confidence = scores[classID]

				# filter out weak predictions by ensuring the detected
				# probability is greater than the minimum probability
				if confidence > 0.5: #args["confidence"]:
					# scale the bounding box coordinates back relative to the
					# size of the image, keeping in mind that YOLO actually
					# returns the center (x, y)-coordinates of the bounding
					# box followed by the boxes' width and height
					box = detection[0:4] * np.array([W, H, W, H])
					(centerX, centerY, width, height) = box.astype("int")

					# use the center (x, y)-coordinates to derive the top and
					# and left corner of the bounding box
					x = int(centerX - (width / 2))
					y = int(centerY - (height / 2))

					# update our list of bounding box coordinates, confidences,
					# and class IDs
					boxes.append([x, y, int(width), int(height)])
					confidences.append(float(confidence))
					classIDs.append(classID)

		# apply non-maxima suppression to suppress weak, overlapping bounding
		# boxes
		idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)#args["confidence"], args["threshold"])

		# ensure at least one detection exists
		detections = Detection2DArray()
		if len(idxs) > 0:
			# loop over the indexes we are keeping
			for i in idxs.flatten():

				# extract the bounding box coordinates
				(x, y) = (boxes[i][0], boxes[i][1])
				(w, h) = (boxes[i][2], boxes[i][3])

				# draw a bounding box rectangle and label on the image
				color = [int(c) for c in COLORS[classIDs[i]]]
				cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
				text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
				cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

				detection = Detection2D()
				res = ObjectHypothesisWithPose()
				res.id = classIDs[i]
				res.score = confidences[i]
				res.pose.pose.position.x = x
				res.pose.pose.position.y = y
				detection.results.append(res)
				bbx = BoundingBox2D()
				bbx.center.x = x
				bbx.center.y = y
				bbx.size_x = w
				bbx.size_y = h
				detection.bbox = bbx
				detections.detections.append(detection)

		# 2: Convert the annotated image to ROS image and publish it. Remove the code visualizing the image in OpenCV
		#cv2.imshow("Image", image)
		#cv2.waitKey(0)
		try:
			image = self.bridge.cv2_to_imgmsg(image)
			self.publisher_image.publish(image)
		except CvBridgeError as e:
			print(e)

		# 3: Add the code that publishes raw detections
		self.publisher_detection.publish(detections)


def main(args):
	ic = image_converter()
	rospy.init_node('labrob_detector', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)