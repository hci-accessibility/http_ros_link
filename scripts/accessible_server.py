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
	setCostMap = rospy.ServiceProxy('navfn_node',SetCostMap.srv)

	#
	# used only for demo. The lengths, widths and costMaps are hard-coded
	#
	if (prof.effective_width == 12 && prof.effective_length == 12) :  
		#setCostMap(costs, height, width) #apply costmap for barrier profile 1
	elif (prof.effective_width == 10 && prof.effective_length == 20) :  
		#setCostMap(costs, height, width) #apply costmap for barrier profile 2
	else :  
		#setCostMap(costs, height, width) #apply costmap for default barrier profile


	print prof
	return

def handle_Navigate_XY_XY(req):
	print req
	Apply_Profile(req.profile)

	#creates a function to get the path
	getPath = rospy.ServiceProxy('navfn_node',MakeNavPlan.srv)
    try:
    	# gets path plan
		resp = getPath(req.start, req.end)
		if resp.foundPath == 1 #if a viable path is found
			path_pose = resp.path  # stores found path

		 # transforms path from pose coordinates to mapCoords
			path_mapCoord = [MapCoord()] * len(path_pose)
			for i in range(len(path_pose))
				path_mapCoord[i].point = path_pose[i].pose.position
				path_mapCoord[i].map_id = 0

			return path_mapCoord # return path

       except rospy.ServiceException, e: 

    return null #define return null if valid path was not created


def accessible_server():
    rospy.init_node('nav_link_server')
    s = rospy.Service('ApplyProfile', Apply_Profile, handle_ApplyProfile)
    print "Ready to revice requests."
    rospy.spin()

if __name__ == "__main__":
    nav_link_server()
