#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import rospy
from dynamixel_msgs.msg import JointState


def callback(data):
    rospy.loginfo(rospy.get_name() + ": Curr_pos is %s" % data.current_pos)


def test_listener():
    rospy.init_node('test_listener', anonymous=True)
    rospy.Subscriber("/tilt_controller1/state", JointState, callback)
    rospy.spin()


if __name__ == '__main__':
    test_listener()
