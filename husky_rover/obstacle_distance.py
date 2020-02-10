#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
	obstacle_distance = msg.ranges[len(msg.ranges)/2]
	print "obstacle distance ahead: %0.1f" % range_ahead

rospy.init_node('obstacle_distance')
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.spin()
