#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def stringCallback(msg):
	print(msg.data)
rospy.init_node('my_sub')
rospy.Subscriber('my_topic', String, stringCallback)
rospy.spin()
