#!/usr/bin/env python
#import roslib; roslib.load_manifest('my_dynamixel_tutorial')
import rospy
from std_msgs.msg import Float64
import math
import numpy as np
import time


if __name__ == '__main__':
    try:

       # x = 0
       # y = 500
       # z = 500
        x = input("Enter x co-ord: ")
        x = float(x)
        y = input("Enter y co-ord: ")
        y = float(y)
        z = input("Enter z co-ord: ")
        z = float(z)
                

        theta6= -1.1    #MANIPULATOR OPEN CLOSE ANGLE in sim frame
        Theta6 = theta6  #MANIP OPEN CLOSE ANGLE in arm frame with offsets
        #Set link lengths

        length1 = 75 #25  
        length2 = 404 #475
        length3 = 345 #380
        length4 = 45 #80
        length5 = 185 #150

        #length1 = 25  
        #length2 = 475
	#length3 = 380
	#length4 = 80
	#length5 = 150


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
		theta1 = math.atan2(y,x)  #BASE ANGLE in simulation frame
		           
		a = dist - length5
		b = z - length1
		R = (a**2 + b**2)**0.5
		Alpha = math.atan2(b,a)
	#	print "alpha", Alpha
		cos2plusalpha = (b**2 + length2**2 + a**2  - (length3 + length4)**2 )/(2*length2*R)


		theta2 = math.acos(cos2plusalpha) + Alpha #MX106 ANGLE in sim frame
		theta3 = math.asin((b-length2*math.sin(theta2))/(length3+length4)) - theta2   #MX64 ANGLE in sim frame
		theta4 = 0  #Hand Twist ANGLE in sim frame
		theta5 = -(theta2+theta3) #Hand up down Angle in sim frame
		Theta = [theta1, theta2, theta3, theta4, theta5, theta6]   #temp collection of theta to store and check in sim frame
	#	print Theta
	#        print theta1, theta2, theta3, theta4, theta5
	#    % Calculate the relative cartesian positions of all joints based on the 
	#    % calculated angles and given link lengths

############################################################################	    
#			Relative transforms
############################################################################
		H01 = np.array([[math.cos(theta1), -math.sin(theta1), 0, 0], [math.sin(theta1), math.cos(theta1), 0, 0], [0, 0, 1, 0],[0, 0, 0, 1]])
		H12 = np.array([[math.cos(theta2), -math.sin(theta2), 0, 0], [0, 0, -1, 0], [math.sin(theta2), math.cos(theta2), 0, length1], [0, 0, 0, 1]])
		H23 = np.array([[math.cos(theta3), -math.sin(theta3), 0, length2], [math.sin(theta3), math.cos(theta3), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
		H34 = np.array([[0, 0, 1, length3],[math.cos(theta4), -math.sin(theta4), 0, 0],[math.sin(theta4), math.cos(theta4), 0, 0], [0, 0, 0, 1]])
		H45 = np.array([[math.sin(theta5), math.cos(theta5), 0, 0],[ 0, 0, 1, 0],[math.cos(theta5), -math.sin(theta5), 0, length4],[0, 0, 0, 1]])
		H5M = np.array([[1, 0, 0, length5],[ 0, 1, 0, 0],[ 0, 0, 1, 0],[ 0, 0, 0, 1]])
	#        print H01,"....",H12,"....",H23,"....",H34,"....",H45,"....",H5M
	#    % Calculate the position of each joint with respent to the original
	#    % coordinate frame

############################################################################

############################################################################
#			Absolute Transforms (wrt base)
############################################################################		


		H02 = np.dot(H01,H12)
		H03 = np.dot(H02,H23)
		H04 = np.dot(H03,H34)
		H05 = np.dot(H04,H45)
		H0M = np.dot(H05,H5M)
###########################################################################

###########################################################################
#			Theta in arm frame (with offset adjustments)
###########################################################################
		
		Theta1 = theta1
		Theta2 = -theta2+2.33
		Theta3 = -theta3+2.33
		Theta4 = theta4;
		Theta5 = -theta5+1.596

		theta = np.array([Theta1, Theta2, Theta3, Theta4, Theta5, Theta6])*1000
                theta = theta.astype(int)/1000.
                theta=theta[::-1]   #In matlab code joint1 = base, but for motor code joint 1 = end-effector, so reversing values

##########################################################################


		if Theta3 > 4.325 or Theta2 < 0.38:   #------------------------------------------Write more for this for all motors-----------------------------#
		    print "Unachievable states"
                else:

	#        print theta
    		    
		
		    
	#        theta=theta + np.array([0,,0,,,-1.64])  
	            
                    mot_pub2(Theta6,Theta5,Theta4,Theta3,Theta2,Theta1)

	#    Check if a solution exists
            except ValueError,exc0bj:
		msg=str(exc0bj)
		if msg == "math domain error":
		    print "Co-ords are out of robots workspace"
		    theta = None

	print "Theta", theta


    except rospy.ROSInterruptException:
        pass

