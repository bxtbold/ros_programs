#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
rospy.init_node('live_streaming', anonymous=True)
class streaming:
	def __init__(self):
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/ardrone/front/image_raw",Image,self.callback, queue_size = 1)
	def callback(self,msg):
		cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
		cv2.imshow("Image window", cv_image)
		cv2.waitKey(3)
live_streaming = streaming()
rospy.spin()
