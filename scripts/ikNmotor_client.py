#!/usr/bin/env python
import roslib; roslib.load_manifest('my_dynamixel_tutorial')

import sys

import rospy
from my_dynamixel_tutorial.srv import *
import csv

def ikNmotor_client(x, y, z):
    rospy.wait_for_service('ikNmotor')
    try:
        ikNmotor = rospy.ServiceProxy('ikNmotor', IkNMotor)
        resp1 = ikNmotor(x, y,z)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
#    if len(sys.argv) == 4:
#        x = int(sys.argv[1])
#        y = int(sys.argv[2])
#        z = int(sys.argv[3])
    while True:       
        
            print 'here'
            with open("/home/ssr/fuerte_workspace/sandbox/send.txt") as f:
                c=csv.reader(f,delimiter=' ',skipinitialspace=True)
                print 'read value'
                for line in c:
                    print 'line is',line
                    a=int(line[0])
                print 'a is',a
                while a==0:
                    print 'waiting for data since a is',a
                    c=csv.reader(f,delimiter=' ',skipinitialspace=True)
                    for line in c:
                        a=int(line[0])
                with open("/home/ssr/fuerte_workspace/sandbox/output.txt") as f:
                    c=csv.reader(f,delimiter=' ',skipinitialspace=True)
                    for line in c:
                        a=line
                    x=float(a[0])
                    y=float(a[1])
                    z=float(a[2])
                    print x,y,z
                    print 'success till here'
                    #f=open("/home/ssr/fuerte_workspace/sandbox/send.txt","w")
                    #f.write(str(0))
                    #f.close()
        
#    else:
#        print usage()
#        sys.exit(1)
            print "Requesting thetas for %f,%f,%f"%(x, y, z)
            print "[%s, %s, %s] = Theta (%s)"%(x, y, z, ikNmotor_client(x, y, z))