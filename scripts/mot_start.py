#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import rospy
import time
from std_msgs.msg import Float64


def mot_start():
    pub1 = rospy.Publisher('tilt_controller1/command', Float64)
    pub2 = rospy.Publisher('tilt_controller2/command', Float64)
    pub3 = rospy.Publisher('tilt_controller3/command', Float64)
    pub4 = rospy.Publisher('tilt_controller4/command', Float64)
    pub5 = rospy.Publisher('tilt_controller5/command', Float64)
    pub6 = rospy.Publisher('tilt_controller6/command', Float64)
    
    rospy.init_node('mot_start')

    xxx=1
    while xxx is 1: #rospy.is_shutdown():
        xxx = 2
        m_three=-1.319
        m_four=2.55
        m_five=0
        m_one=2.03
        m_two=1.225
        m_six=-1.850  #-1.996

        #str = "hello world %s" % rospy.get_time()
        rospy.loginfo(m_one)
        rospy.loginfo(m_two)
        rospy.loginfo(m_three)
        rospy.loginfo(m_four)
        rospy.loginfo(m_five)
        rospy.loginfo(m_six)

        pub1.publish(Float64(m_one))
        pub2.publish(Float64(m_two))
        time.sleep(1)
        pub6.publish(Float64(m_six))
#        print "moving base"
        time.sleep(1)
        pub3.publish(Float64(m_three))
        pub4.publish(Float64(m_four))
        pub5.publish(Float64(m_five))
	
        rospy.sleep(0.1)


if __name__ == '__main__':
    try:
#        time.sleep(1)
        mot_start()
    except rospy.ROSInterruptException:
        pass
