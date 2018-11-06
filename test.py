#! /usr/bin/env python

import logging
import time
import rospy
from darknet_ros_msgs.msg import BoundingBoxes

def callback(msg):
	print msg.bounding_boxes

rospy.init_node('test')

sub = rospy.Subscriber('darknet_ros/bounding_boxes', BoundingBoxes, callback)

rospy.spin()