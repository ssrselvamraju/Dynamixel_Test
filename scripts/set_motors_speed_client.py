#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import sys

import rospy

from my_dynamixel_tutorial.srv import *
from dynamixel_controllers.srv import *



def set_motor_speeds_client():
    rospy.wait_for_service('/tilt_controller1/set_speed')
    rospy.wait_for_service('/tilt_controller2/set_speed')
    rospy.wait_for_service('/tilt_controller3/set_speed')
    rospy.wait_for_service('/tilt_controller4/set_speed')
    rospy.wait_for_service('/tilt_controller5/set_speed')
    rospy.wait_for_service('/tilt_controller6/set_speed')
    
    try:
        set_speed1 = rospy.ServiceProxy('/tilt_controller1/set_speed', SetSpeed)
        set_speed1(0.25)
        set_speed2 = rospy.ServiceProxy('/tilt_controller2/set_speed', SetSpeed)
        set_speed2(0.2)
        set_speed3 = rospy.ServiceProxy('/tilt_controller3/set_speed', SetSpeed)
        set_speed3(0.25)
        set_speed4 = rospy.ServiceProxy('/tilt_controller4/set_speed', SetSpeed)
        set_speed4(0.3)
        set_speed5 = rospy.ServiceProxy('/tilt_controller5/set_speed', SetSpeed)
        set_speed5(0.3)
        set_speed6 = rospy.ServiceProxy('/tilt_controller6/set_speed', SetSpeed)
        set_speed6(0.25)
    except rospy.ServiceException, e:
        print "Setting motor speed failed, ERROR: %s"%e


if __name__ == "__main__":
       print "Setting motor speeds"
       set_motor_speeds_client()
       
       

