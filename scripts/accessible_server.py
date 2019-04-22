#!/usr/bin/env python

from accessible_navigator.srv import *
from accessible_navigator.msg import *
import rospy

# ~~~~~~~~~~ Routing Fundamentals 
# THESE ARE HELPER FUNCTIONS, NOT SERVICES

def Apply_Profile(prof):
	# PSQL select relevant STRICT barriers from the DB
	# PSQL should also do partials and user specific ones, but not important right now

	#get occupancy map from 

	if prof        :  
		#apply barrier profile 1
	elif           :
		#apply barrier profile 2
	elif           :
		#apply barrier profile 3




	print prof
	return

def handle_Navigate_XY_XY(req):
	print req
	
	#set_base to req.start
	Apply_Profile(req.profile)

	return goto_XY(req.end) 

def goto_XY(end):
	path = [] #call the thing that returns the path with end as the parameter
	return path


def nav_link_server():
    rospy.init_node('nav_link_server')
    s = rospy.Service('ApplyProfile', Apply_Profile, handle_ApplyProfile)
    print "Ready to revice requests."
    rospy.spin()

if __name__ == "__main__":
    nav_link_server()
