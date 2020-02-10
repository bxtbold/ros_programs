#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('take_off', anonymous=True) # creating a node as fly_to_position
twist = Twist()        															# using Twist class from cmd_vel
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)  #publishing the position 
go = Twist()
to_time = time.time()
go.angular.x = 0; go.angular.y = 0; go.angular.z = 0
# x,y,z = input('(x,y,z): ').split()
while True:
    go = Twist()
    go.linear.x = 0; go.linear.y = 0; go.linear.z = 0.1
    pub.publish(go)
    while time.time() - to_time > 0.5:
        go.linear.x = 0; go.linear.y = 0; go.linear.z = 0
        pub.publish(go)
