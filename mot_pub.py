#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import rospy
from std_msgs.msg import Float64


def mot_pub():
    pub1 = rospy.Publisher('tilt_controller1/command', Float64)
    pub2 = rospy.Publisher('tilt_controller2/command', Float64)
    pub3 = rospy.Publisher('tilt_controller3/command', Float64)
    pub4 = rospy.Publisher('tilt_controller4/command', Float64)
    pub5 = rospy.Publisher('tilt_controller5/command', Float64)
    pub6 = rospy.Publisher('tilt_controller6/command', Float64)
    
    rospy.init_node('mot_publisher')

    while not rospy.is_shutdown():
	m_three=input("Enter the angle for first motor - end effector")
	m_three=float(m_three)
	m_four=input("Enter the angle for second motor")
	m_four=float(m_four)
	m_five=input("Enter the angle for third motor")
	m_five=float(m_five)
	m_one=input("Enter the angle for fourth motor")
	m_one=float(m_one)
	m_two=input("Enter the angle for fifth motor")
	m_two=float(m_two)
	m_six=input("Enter the angle for sixth motor - base")
	m_six=float(m_six)

        #str = "hello world %s" % rospy.get_time()
	rospy.loginfo(m_one)
	rospy.loginfo(m_two)
	rospy.loginfo(m_three)
	rospy.loginfo(m_four)
	rospy.loginfo(m_five)
	rospy.loginfo(m_six)

        pub1.publish(Float64(m_one))
	pub2.publish(Float64(m_two))
        pub3.publish(Float64(m_three))
	pub4.publish(Float64(m_four))
        pub5.publish(Float64(m_five))
	pub6.publish(Float64(m_six))

	rospy.sleep(0.1)


if __name__ == '__main__':
    try:
        mot_pub()
    except rospy.ROSInterruptException:
        pass
