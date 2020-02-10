#!/usr/bin/env python
import rospy
from std_msgs.msg import String
rospy.init_node('my_pub')
pub = rospy.Publisher('my_topic', String, queue_size = 10)
topic_content = ' Hello World! '
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	pub.publish(topic_content)
	rate.sleep()
