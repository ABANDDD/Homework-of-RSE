#!/usr/bin/env python
import rospy
import aiml
import os
import sys
from std_msgs.msg import String

rospy.init_node('voice_server')
mybot = aiml.Kernel()
response_publisher = rospy.Publisher('response', String, queue_size=10)

def load_aiml(xml_file):
    data_path = rospy.get_param("aiml_path")
    print data_path
    os.chdir(data_path)
    if os.path.isfile("standard.brn"):
        mybot.bootstrap(brainFile="standard.brn")
    else:
        mybot.bootstrap(learnFiles=xml_file, commands="load aiml b")
        mybot.saveBrain("standard.brn")

def callback(data):

    Input=data.data
    response=mybot.respond(Input)
    rospy.loginfo("I heard %s",data.data)
    print "I said %s",response
    response_publisher.publish(response)

def listener():
    rospy.loginfo("Starting server")
    rospy.Subscriber("voicewords",String,callback)
    rospy.spin()


if __name__=='__main__':
    load_aiml('startup.xml')
    listener()
