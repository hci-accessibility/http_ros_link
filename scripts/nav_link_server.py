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

	print prof
	return

def get_XY_for_Room(building_id, room_id)
	print(building_id, room_id)
	#psql: get the map tag id from the rooms table
	# ask rtabmap's services for location of map tag id?
	return (1,1)

def checkClear_R(building_id, room_id):
	coords = get_XY_for_Room(req.building, ????, req.room)
	Apply_Profile(req.profile)
	#ask costmap if literally overlapping a full barrier?
	# ask costmap for nearby values, sum them & threshold
	return #bool assessment of if clarification is needed


# ~~~~~~~~~~~~~~~~~NAVIGATION~~~~~~~~~~~~~~~
# THESE ARE ACTUAL SERVICES
def handle_Navigate_R_R(req):
	Apply_Profile(req.profile);
	if(!checkClear_R(req.start_building, req.start_room))
		# we need to request clarification of start
	if(!checkClear_R(req.goal_building,req.goal_room))
		#need to clarify that one too

	coords_start = get_XY_for_Room(req.start_building, req.start_room)
	coords_end = get_XY_for_Room(req.goal_building, req.goal_room)

	#place self at coords start Via RTABMAP_ROS's ResetPose service


	print req
	return

def handle_Navigate_XY_XY(req):
	print req
	return

def nav_link_server():
    rospy.init_node('nav_link_server')
    s = rospy.Service('ApplyProfile', Apply_Profile, handle_ApplyProfile)
    print "Ready to revice requests."
    rospy.spin()

if __name__ == "__main__":
    nav_link_server()
