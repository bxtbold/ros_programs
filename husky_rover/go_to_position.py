#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import math
# initial robot position
x = 0.0
y = 0.0
angle = 0.0

def position(msg):       # receives msg from odom and stores the current position of the robot
        global x
        global y
        global angle
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        ang = msg.pose.pose.orientation
        (roll,pitch,angle) = euler_from_quaternion([ang.x,ang.y,ang.z,ang.w])

rospy.init_node('go_to_position')   # creating a node and naming it go_to_position
 
subscribing = rospy.Subscriber('/odometry/filtered', Odometry, position)     # subscribing the msg
publishing = rospy.Publisher('/cmd_vel', Twist, queue_size=1)                # publishing where to go
rate = rospy.Rate(5)      		  # rospy rate with 5 hertz (sends 5 msgs per second)

# goal position
goal_x = 5
goal_y = 5

# Creating rotation around z-axis and going forward 
go = Twist()

while not rospy.is_shutdown():
	# the distance in terms of x and y axises
        loc_x = goal_x - x
        loc_y = goal_y - y
        # the angle from the current position to the goal position with the respect to x-axis
        rotation = math.atan(loc_y/loc_x)
 
        if abs(rotation - angle) > 0.1:     # if destination is not in the robot direction
                go.linear.x = 0.0
                go.angular.z = 0.5          # rotate with speed of 0.5
        else:                               # if the robot is in the robot direction
                go.linear.x = 1.0           # go forward with speed of 1
                go.angular.z = 0.0
 
        publishing.publish(go)              # publishing as go
        rate.sleep()                        # end of the loop






