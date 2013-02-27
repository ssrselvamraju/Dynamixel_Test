#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import rospy
from std_msgs.msg import Float64


def mot_pub():
    pub1 = rospy.Publisher('tilt_controller1/command', Float64)
    pub2 = rospy.Publisher('tilt_controller2/command', Float64)
    rospy.init_node('mot_publisher')

    while not rospy.is_shutdown():
	x=input("Enter the angle for first motor")
	x=float(x)
	y=input("Enter the angle for second motor")
	y=float(y)
        #str = "hello world %s" % rospy.get_time()
	rospy.loginfo(x)
	rospy.loginfo(y)
        pub1.publish(Float64(x))
	pub2.publish(Float64(y))
	rospy.sleep(0.1)


if __name__ == '__main__':
    try:
        mot_pub()
    except rospy.ROSInterruptException:
        pass
