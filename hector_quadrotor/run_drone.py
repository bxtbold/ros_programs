#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('fly_to_position', anonymous=True) # creating a node as fly_to_position
twist = Twist()       				# using Twist class from cmd_vel
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)  #publishing the position 

go = Twist()
ticks = time.time()

while True:
    go = Twist()
    go.linear.x = 0.5; go.linear.y = 0.5; go.linear.z = 0.5
    go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
    pub.publish(go)
    if time.time() - ticks > 4.0:
        while True:
            go.linear.x = 0; go.linear.y = 0; go.linear.z = 0
            go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
            pub.publish(go)
            if time.time() - ticks > 6.0:
                break
        break
ticks = time.time()
while True:
    go = Twist()
    go.linear.x = -0.5; go.linear.y = -0.5; go.linear.z = 0
    go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
    pub.publish(go)
    if time.time() - ticks > 3.47:
        while True:
            go.linear.x = 0; go.linear.y = 0; go.linear.z = 0
            go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
            pub.publish(go)
            if time.time() - ticks > 5.0:
                break
        break
while True:
    go = Twist()
    go.linear.x = 0; go.linear.y = 0; go.linear.z = -0.5
    go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
    pub.publish(go)
