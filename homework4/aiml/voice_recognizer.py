#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('voice_recognizer')
pub=rospy.Publisher('voicewords',String,queue_size=10)
r=rospy.Rate(1)

def get_voice(data):
  voice_text=data.data
  rospy.loginfo("I said::%s",voice_text)
  pub.publish(voice_text)
def listener():
  rospy.loginfo("starting voice recognizing")
  rospy.Subscriber("/lm_data", String, get_voice)
  rospy.spin()
while not rospy.is_shutdown():
  listener()	
