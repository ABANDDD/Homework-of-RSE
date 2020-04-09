#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from opencv_apps.msg import FaceArrayStamped
import os
from sound_play.libsoundplay import SoundClient

state = True

def callback(data):
    global state
    i = data.header.seq
    x = 0
    y = 0
    soundhandle = SoundClient()
    for samples in data.faces:
        x = samples.face.x
        y = samples.face.y
        print(x,y)
    if x < 250:
        soundhandle.say('go right')
    if x > 300:
        soundhandle.say('go left')
    if x > 250 and state == True and x<300:
        os.system("python /home/dingye/catkin_ws/src/rc-home-edu-learn-ros/rchomeedu_vision/scripts/take_photo.py")
        state = False



def listen(data):
    text = data.data
    if text=='TAKE PHOTO':
        state = True
        print "start now"
        rospy.init_node("location",anonymous=True)
        rospy.Subscriber("/face_detection/faces",FaceArrayStamped,callback)
        rospy.spin()


def listens():
    rospy.init_node("location",anonymous=True)
    rospy.loginfo("start mission")
    rospy.Subscriber("/lm_data",String,listen)
    rospy.spin()

if __name__=='__main__':
    listens()