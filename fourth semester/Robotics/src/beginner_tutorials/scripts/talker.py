import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist, Point
import math

class Turtle:

    def __init__(self):

        rospy.init_node('talker', anonymous=True)
        self.goal = Point()
        self.pose = Pose()

        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.goal_sub = rospy.Subscriber('/turtle1/goal', Point, self.get_goal_pose)

    def get_goal_pose(self, msg):

        self.goal.x = msg.x
        self.goal.y = msg.y
        self.goal.z = msg.z

    def callback(self, data):

        self.pose = data

    def get_euclidean_distance(self, pose, goal):
        return math.sqrt((self.pose.x - self.goal.x)**2 + (self.pose.y - self.goal.y)**2)

    def move(self):
        
        self.rate = rospy.Rate(10)
        move = Twist()
        
        while not rospy.is_shutdown() or self.get_euclidean_distance(self.pose, self.goal) > 0.1:
            
            x_move = self.goal.x - self.pose.x
            y_move = self.goal.y - self.pose.y

            if abs(math.atan2(y_move, x_move) - self.pose.theta) > 0.1:
                move.linear.x = 0.0
                move.angular.z = 0.3
            else:
                move.linear.x = 0.5
                move.angular.z = 0.0
                
            if self.get_euclidean_distance(self.pose, self.goal) > 0.1:
                rospy.loginfo("Current position of the turtle: [ x: %f, y: %f ]"%(self.pose.x, self.pose.y))
            else:
                move.linear.x = 0.0
                move.angular.z = 0.0
            
            self.publisher.publish(move)
            self.rate.sleep()
        rospy.spin()
        
if __name__ == '__main__':
    try:
        tur = Turtle()
        tur.move()
    except rospy.ROSInterruptException:
        pass


