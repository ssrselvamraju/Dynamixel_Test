#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from std_msgs.msg import String
import math
import numpy as np
import time
import copy
#import sys
from dynamixel_controllers.srv import *
from my_dynamixel_tutorial.srv import *
from dynamixel_msgs.msg import JointState


###########GLOBAL VARIABLES###############
global stop_command

stop_command = "start"

global gripper_angle

gripper_angle = 0.0

global ui_flag

ui_flag = 0
##########################################



def mot_pub(m_three,m_four,m_five,m_one,m_two,m_six):
    pub1 = rospy.Publisher('tilt_controller1/command', Float64)
    pub2 = rospy.Publisher('tilt_controller2/command', Float64)
    pub3 = rospy.Publisher('tilt_controller3/command', Float64)
    pub4 = rospy.Publisher('tilt_controller4/command', Float64)
    pub5 = rospy.Publisher('tilt_controller5/command', Float64)
    pub6 = rospy.Publisher('tilt_controller6/command', Float64)
    
    
#    rospy.init_node('mot_publisher')
    xxx=1
    while xxx is 1: #rospy.is_shutdown():
        xxx = 2
        m_three=float(m_three)
        m_four=float(m_four)
        m_five=float(m_five)
        m_one=float(m_one)
        m_two=float(m_two)
        m_six=float(m_six)

        rospy.loginfo(m_six) #Base

        rospy.loginfo(m_one)  #MX-64
        rospy.loginfo(m_two)  #MX-106?

        rospy.loginfo(m_three)  #End effector open close
        rospy.loginfo(m_four)  #End effector up/down
        rospy.loginfo(m_five)  #End effector twist

#Order in which stuff is published
        time.sleep(1)
        pub2.publish(0.57)
        print "MX 106 at", 0.57*180/math.pi, "degrees"
        pub1.publish(Float64(m_one))
        print "MX 64 at", m_one*180/math.pi, "degrees"
        time.sleep(1)
        pub3.publish(Float64(m_three))
        pub4.publish(Float64(m_four))
        pub5.publish(Float64(m_five))
        time.sleep(1)
        pub6.publish(Float64(m_six))
        print "Moving base", "m_six", m_six
#        time.sleep(1)
#        pub1.publish(Float64(m_one))
        time.sleep(2)  #Increase delay while its working
        print "MX 106 at", m_two*180/math.pi, "degrees"

        pub2.publish(Float64(m_two))
#        time.sleep(1)
        
        rospy.sleep(0.1)
        time.sleep(5)
#add something to read current state of motors and check if reached desired position


#see if rosspin shud be added here
    return None

def pickme_ik(x,y,z):
       # x = 0
       # y = 500
       # z = 500

        theta6= -1   #setting manip approach angle 
        Theta6 = theta6
        #Set link lengths

        length1 = 75 #25  
        length2 = 404 #475
        length3 = 345 #380
        length4 = 45 #80
        length5 = 185 #150

         #print 'length1', length1, length2

         #%Calculate the "shadow length" from the object to the robot base
        dist = (((x**2)+(y**2))**(0.5))
        #print dist
        #Check if the selected coordinates are possible given link lengths

        if (dist**2+z**2)**0.5 > (length1+length2+length3+length4+length5):
    #    % Set the robot arm to be reaching straight out if the user input
    #    % isn't possible
            print "'These coordinates are out of the robots workspace','Coordinate error'"
            theta = None

        else:

    #    % Calculate the angular position of all joints
            try:
                theta1 = math.atan2(y,x)
                   
                a = dist - length5
                b = z - length1
                R = (a**2 + b**2)**0.5
                Alpha = math.atan2(b,a)
    #    print "alpha", Alpha
                cos2plusalpha = (b**2 + length2**2 + a**2  - (length3 + length4)**2 )/(2*length2*R)
                theta2 = math.acos(cos2plusalpha) + Alpha
                theta3 = math.asin((b-length2*math.sin(theta2))/(length3+length4)) - theta2
                theta4 = 0
                theta5 = -(theta2+theta3)
                Theta = [theta1, theta2, theta3, theta4, theta5, theta6]
    #    print Theta
    #        print theta1, theta2, theta3, theta4, theta5

    
    #    % Calculate the relative cartesian positions of all joints based on the 
    #    % calculated angles and given link lengths

        
                H01 = np.array([[math.cos(theta1), -math.sin(theta1), 0, 0], [math.sin(theta1), math.cos(theta1), 0, 0], [0, 0, 1, 0],[0, 0, 0, 1]])
                H12 = np.array([[math.cos(theta2), -math.sin(theta2), 0, 0], [0, 0, -1, 0], [math.sin(theta2), math.cos(theta2), 0, length1], [0, 0, 0, 1]])
                H23 = np.array([[math.cos(theta3), -math.sin(theta3), 0, length2], [math.sin(theta3), math.cos(theta3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
                H34 = np.array([[0, 0, 1, length3],[math.cos(theta4), -math.sin(theta4), 0, 0],[math.sin(theta4), math.cos(theta4), 0, 0], [0, 0, 0, 1]])
                H45 = np.array([[math.sin(theta5), math.cos(theta5), 0, 0],[ 0, 0, 1, 0],[math.cos(theta5), -math.sin(theta5), 0, length4],[0, 0, 0, 1]])
                H5M = np.array([[1, 0, 0, length5],[ 0, 1, 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]])

#        H5M = np.array([[1, 0, 0, length5],[ 0, 1, 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]])
    #        print H01,"....",H12,"....",H23,"....",H34,"....",H45,"....",H5M
    #    % Calculate the position of each joint with respent to the original
    #    % coordinate frame
        
                H02 = np.dot(H01,H12)
                H03 = np.dot(H02,H23)
                H04 = np.dot(H03,H34)
                H05 = np.dot(H04,H45)
                H0M = np.dot(H05,H5M)
        
        
                Theta1 = theta1     # BASE
                Theta2 = -theta2+2.33    #MX106
                Theta3 = -theta3+2.33   #MX64
                Theta4 = theta4     #ARM twist 
                Theta5 = theta5+1.596   #Arm up/down  #Check and change this value in all the programs


                theta = np.array([Theta1, Theta2, Theta3, Theta4, Theta5, Theta6])*1000
                theta = theta.astype(int)/1000.
                theta=theta[::-1]   #In matlab code joint1 = base, but for motor code joint 1 = end-effector, so reversing values


                if Theta2 < 0.55 or Theta2 > 2.4 or Theta3 < 0.48 or Theta3 > 4.3 or Theta5 < -0.1 or Theta5 > 2.606 :  
                    print "Position unreachable by motors"
                else:
                    print theta
    #        theta=theta + np.array([0,,0,,,-1.64])  
                    return theta
#                    mot_pub(Theta6,Theta5,Theta4,Theta3,Theta2,Theta1)


            except ValueError,exc0bj:
                msg=str(exc0bj)
                if msg == "math domain error":
                    print "Co-ords are out of robots workspace"
                theta = None
    

def setMotorSpeeds_client():
    rospy.wait_for_service('/tilt_controller1/set_speed')
    rospy.wait_for_service('/tilt_controller2/set_speed')
    rospy.wait_for_service('/tilt_controller3/set_speed')
    rospy.wait_for_service('/tilt_controller4/set_speed')
    rospy.wait_for_service('/tilt_controller5/set_speed')
    rospy.wait_for_service('/tilt_controller6/set_speed')
    print "Setting motor speeds"
    try:
        set_speed1 = rospy.ServiceProxy('/tilt_controller1/set_speed', SetSpeed)
        set_speed1(0.25)
        set_speed2 = rospy.ServiceProxy('/tilt_controller2/set_speed', SetSpeed)
        set_speed2(0.10)
        set_speed3 = rospy.ServiceProxy('/tilt_controller3/set_speed', SetSpeed)
        set_speed3(0.25)
        set_speed4 = rospy.ServiceProxy('/tilt_controller4/set_speed', SetSpeed)
        set_speed4(0.35)
        set_speed5 = rospy.ServiceProxy('/tilt_controller5/set_speed', SetSpeed)
        set_speed5(0.35)
        set_speed6 = rospy.ServiceProxy('/tilt_controller6/set_speed', SetSpeed)
        set_speed6(0.25)
    except rospy.ServiceException, e:
        print "Setting motor speed failed, ERROR: %s"%e


#'''

##################################################################
######Function to set complaince####################
#Measure and set stuff from Windows!!!

def setMotorComplaince_client():
    rospy.wait_for_service('/tilt_controller3/set_compliance_slope')   #Complaince slope
    rospy.wait_for_service('/tilt_controller3/set_compliance_margin')   #Complaince margin
    
    try:
        print "Setting compliance"
        set_speed3 = rospy.ServiceProxy('/tilt_controller3/set_compliance_slope', SetComplianceSlope)
        set_speed3(4)
        set_speed3 = rospy.ServiceProxy('/tilt_controller3/set_compliance_margin', SetComplianceMargin)
        set_speed3(4)

    
    except rospy.ServiceException, e:
        print "Setting motor compliance failed, ERROR: %s"%e




##################################################################

##################################################################
######Function to set motor torque####################


def setMotorTorque_client():
    rospy.wait_for_service('/tilt_controller3/torque_enable')
    
    try:
        torque_enable3 = rospy.ServiceProxy('/tilt_controller3/torque_enable', TorqueEnable)
        torque_enable3(0)
        
    except rospy.ServiceException, e:
        print "Setting motor speed failed, ERROR: %s"%e

##################################################################




##################################################################
#    Test progs for arduino integration


def arduino_callback(data):
#    rospy.loginfo(data.data)
    stop_message = data.data
    

def arduino_listener():
#    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("stopMsg", String, arduino_callback)




###################################################################



###################################################################
######Subscribers for gripper position################

def gripper_callback(data):
#    rospy.loginfo("Curr_gripper_pos is %s" % data.current_pos)
    gripper_angle = data.current_pos

def gripper_pos_listener():
#    rospy.init_node('test_listener', anonymous=True)
    rospy.Subscriber("/tilt_controller3/state", JointState, gripper_callback)






####################################################################


#'''


def closeManip(flag):

    manipPub = rospy.Publisher('tilt_controller3/command', Float64)
    xxx=1
    while xxx is 1: #run just once instead of checking #rospy.is_shutdown():
        xxx = 2
        
    if flag == 0:   #CLOSE
        ui_flag=1
        uiPub = rospy.Publisher('toggle_led', Int32)
        uiPub.publish(ui_flag)
        
        manipCloseVal = -1.4
        print "Closing End effector"
        time.sleep(1)
        
        ui_flag=0
        uiPub.publish(ui_flag)
        
        
        
        manipPub.publish(Float64(manipCloseVal))
#        print stop_command
#        if stop_command == "stop":
#            setMotorTorque_client()
#            print "Stopped due to COMMAND"
#        ###grip apple tight!!
#            time.sleep(1)
#            setFinal_gripper_angle = -1.4
##            current_gripper_angle = copy.deepcopy(gripper_angle)
##            setFinal_gripper_angle = current_gripper_angle - 0.08   ###CHECK ####### TEST######put inside if!!
#            
#            manipPub.publish(Float64(setFinal_gripper_angle))

        time.sleep(2)

        ui_flag=3
        uiPub.publish(ui_flag)
        
        
        
        dropFruit()
        
    else:

        ui_flag=4
        uiPub = rospy.Publisher('toggle_led', Int32)
        uiPub.publish(ui_flag)

        
        manipCloseVal = -0.8    #check values
        print "Opening End Effector"
        time.sleep(1)
        manipPub.publish(Float64(manipCloseVal))
        time.sleep(3)
#        rospy.spinonce()
        return None
    
#    time.sleep(1)
    return None
    
    
    
def dropFruit():
    
    pub1 = rospy.Publisher('tilt_controller1/command', Float64)
    pub2 = rospy.Publisher('tilt_controller2/command', Float64)
    pub3 = rospy.Publisher('tilt_controller3/command', Float64)
    pub4 = rospy.Publisher('tilt_controller4/command', Float64)
    pub5 = rospy.Publisher('tilt_controller5/command', Float64)
    pub6 = rospy.Publisher('tilt_controller6/command', Float64)
    
    
#    rospy.init_node('mot_publisher')
    xxx=1
    while xxx is 1: #rospy.is_shutdown():
        xxx = 2
    #define all these values after measurement
    
    
    m_four = 0.785 #rock
    m_five = -0.785 #twist
    
# m_two = 0.7 #come back a bit
    rospy.loginfo(m_four)
    rospy.loginfo(m_five)
# rospy.loginfo(m_two)
    
    
    time.sleep(1)
    
    pub4.publish(Float64(m_four))
    pub5.publish(Float64(m_five))

    time.sleep(1)
    
    
    
    
    
    second_start_angles = pickme_ik(350,0,800)
#    print "Second Start"
    mot_pub(-1.4,second_start_angles[1],second_start_angles[2],second_start_angles[3],second_start_angles[4],second_start_angles[5])
    time.sleep(2)    
#    time.sleep(1)
    
    # Get manip to drop position
    
    m_three=-0.95
    m_four=0.966
    m_five=-0.347
    m_one=4.28
    m_two=1.5
    m_six=-1.917

    
    
#    m_three=float(0)
#    m_four=float(0)
#    m_five=float(0)
#    m_one=float(0)
#    m_two=float(0)
#    m_six=float(0)

    rospy.loginfo(m_six) #Base
    time.sleep(1)
    rospy.loginfo(m_one)  #MX-64
    rospy.loginfo(m_two)  #MX-106?

    rospy.loginfo(m_three)  #End effector open close
    rospy.loginfo(m_four)  #End effector up/down
    rospy.loginfo(m_five)  #End effector twist

#Order in which stuff is published    ##Change this order in this case (may be two positions)

    pub6.publish(Float64(m_six))
    time.sleep(1)
#    print "MX 64 at", m_one*180/math.pi, "degrees"

    pub1.publish(Float64(m_one))
    time.sleep(1)
    pub4.publish(Float64(m_four))
    pub5.publish(Float64(m_five))
    time.sleep(1.5)
    pub2.publish(Float64(m_two))
#    print "MX 106 at", m_two*180/math.pi, "degrees"
    
    time.sleep(3)
#    pub3.publish(Float64(m_three))    #check if needed to uncomment
        
    rospy.sleep(0.1)
#add something to read current state of motors and check if reached desired position
    time.sleep(3)
    closeManip(1)    #open manipulator
    time.sleep(5)

            
    ui_flag=0
    uiPub = rospy.Publisher('toggle_led', Int32)
    uiPub.publish(ui_flag)

    
    f=open("/home/ssr/fuerte_workspace/sandbox/send.txt","w")
    f.write('1')
    f.close()
    
    
######################################################





########################################################
    
    
    return None


def handle_ikNmotor(req):
    
    x = float(req.x)
    y = float(req.y)
    z = float(req.z)
    
    print "X Y Z [%s  %s  %s]"%(x, y, z)    
    motor_angles = pickme_ik(x,y,z)
    print "Motor Angles", motor_angles

    resp = IkNMotorResponse()
    resp.angles=motor_angles
#############################    
    second_start_angles = pickme_ik(350,0,800)
#    print "Second Start"
    mot_pub(second_start_angles[0],second_start_angles[1],second_start_angles[2],second_start_angles[3],second_start_angles[4],second_start_angles[5])
    time.sleep(4)
#############################    
    if motor_angles is not None:
        
        mot_pub(motor_angles[0],motor_angles[1],motor_angles[2],motor_angles[3],motor_angles[4],motor_angles[5])
        time.sleep(3)
        closeManip(0)

    print "Theta", motor_angles

#    Check if arm has reached position



    
    return resp

    
    
    
    
    
    
def ikNmotor_server():
    rospy.init_node('ikNmotor_server')

    gripper_pos_listener()
    arduino_listener()

    ui_flag=2
    uiPub = rospy.Publisher('toggle_led', Int32)
    uiPub.publish(ui_flag)

    
    s = rospy.Service('ikNmotor', IkNMotor, handle_ikNmotor)
    print "Ready to get ik and set motors."
    
    
    rospy.spin()

if __name__ == '__main__':
    setMotorSpeeds_client()
    time.sleep(2)
    setMotorComplaince_client()
    time.sleep(0.5)
    

    try:
        ikNmotor_server()
#        x = input("Enter x co-ord: ")
#        x = float(x)
#        y = input("Enter y co-ord: ")
#        y = float(y)
#        z = input("Enter z co-ord: ")
#        z = float(z)
        
#        motor_angles = pickme_ik(x,y,z)
        
#        if motor_angles is not None:
#            mot_pub(motor_angles[0],motor_angles[1],motor_angles[2],motor_angles[3],motor_angles[4],motor_angles[5])

#        print "Theta", motor_angles

        ui_flag=0
        uiPub = rospy.Publisher('toggle_led', Int32)
        uiPub.publish(ui_flag)



        print "APPLE PICKED AND DROPPED"
    except rospy.ROSInterruptException:
        pass
