#!/usr/bin/env python3
import rospy

import math
import tf2_ros
#import geometry_msgs.msg
import turtlesim.srv
from std_msgs.msg import String  # C
import tf2_msgs.msg  # D
import geometry_msgs.msg # D


if __name__ == '__main__':
    rospy.init_node('shanks_pervert')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # C - publishes String messages of the center of shanks
    publisher_info = rospy.Publisher('shanks_pervert/shanks_center_info', String, queue_size=1)

    # D - publishes tf2 of center of shanks
    publisher_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1)

    rate = rospy.Rate(10.0)
    print("(initialized the shanks pervert, have a good time watching that sweet shanks info)")

    while not rospy.is_shutdown():
        # try get transforms of all shanks, you perv
        try:
            trans_rf = tfBuffer.lookup_transform('RF_SHANK', 'base', rospy.Time())
            trans_lf = tfBuffer.lookup_transform('LF_SHANK', 'base', rospy.Time())
            trans_rh = tfBuffer.lookup_transform('RH_SHANK', 'base', rospy.Time())
            trans_lh = tfBuffer.lookup_transform('LH_SHANK', 'base', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        # compute average of metric position
        avg_x = ( \
            trans_rf.transform.translation.x + \
            trans_lf.transform.translation.x + \
            trans_rh.transform.translation.x + \
            trans_lh.transform.translation.x \
        ) / 4
        
        avg_y = ( \
            trans_rf.transform.translation.y + \
            trans_lf.transform.translation.y + \
            trans_rh.transform.translation.y + \
            trans_lh.transform.translation.y \
        ) / 4

        avg_z = ( \
            trans_rf.transform.translation.z + \
            trans_lf.transform.translation.z + \
            trans_rh.transform.translation.z + \
            trans_lh.transform.translation.z \
        ) / 4

        # (assume RF's orientation for simplicity)

        # handle String info messages publishing
        #   NOTE: This will look ugly in ros, but nice if simply printed
        info_msg = \
            "Coordinate system w. respect to the base:\n" + \
            "\tmetric" + \
            "\n\t\tx: " + str(avg_x) + \
            "\n\t\ty: " + str(avg_y) + \
            "\n\t\tz: " + str(avg_z) + \
            "\n\torientation" + \
            "\n\t\tx: " + str(trans_rf.transform.rotation.x)  + \
            "\n\t\ty: " + str(trans_rf.transform.rotation.y) + \
            "\n\t\tz: " + str(trans_rf.transform.rotation.z) + \
            "\n\t\tw: " + str(trans_rf.transform.rotation.w) + "\n"

        publisher_info.publish(info_msg)  # ugly, but working (could be of type 'Twist' instead, but I kept it like this for simplicity)
        print(info_msg)  # quite pretty

        # handle tf publishing
        t = geometry_msgs.msg.TransformStamped()
        t.header.frame_id = "base"
        t.header.stamp = trans_rf.header.stamp  # rospy.Time.now()
        t.child_frame_id = "CoS"
        # metric
        t.transform.translation.x = avg_x
        t.transform.translation.y = avg_y
        t.transform.translation.z = avg_z
        # orientation
        t.transform.rotation.x = trans_rf.transform.rotation.x
        t.transform.rotation.y = trans_rf.transform.rotation.y
        t.transform.rotation.z = trans_rf.transform.rotation.z
        t.transform.rotation.w = trans_rf.transform.rotation.w
        tfm = tf2_msgs.msg.TFMessage([t])
        publisher_tf.publish(tfm)

        rate.sleep()
