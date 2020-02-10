#!/usr/bin/env python
import rospy
import time
from nav_msgs.msg import Odometry


rospy.init_node('print_position')

def position(msg):
	print('x: ',msg.pose.pose.position.x,', y: ',msg.pose.pose.position.y)
	time.sleep(0.5)
	

sub = rospy.Subscriber('/odom',Odometry,position,queue_size = 1)
rospy.spin()
