#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('land', anonymous=True) # creating a node as land
twist = Twist()        															# using Twist class from cmd_vel
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)  #publishing the position 
go = Twist()

tick = time.time()

while True:
    go = Twist()
    go.linear.x = 0; go.linear.y = 0; go.linear.z = -0.5
    go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
    pub.publish(go)