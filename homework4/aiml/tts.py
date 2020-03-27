#!/usr/bin/env python
import rospy
import os
import sys
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

rospy.init_node('tts', anonymous=True)
soundhandle = SoundClient()
rospy.sleep(10)
#soundhandle.stopALL()
print 'start'

def get_response(data):
    response = data.data
    print response
    soundhandle.say(response, volume=5)

def listener():
    print 'start listening'
    rospy.Subscriber("response",String,get_response,queue_size=10)
    rospy.spin()

if __name__=='__main__':
    listener()
