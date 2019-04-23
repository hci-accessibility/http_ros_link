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
	if prof        :  
		#apply barrier profile 1
		#setCostMap(costs, height, width)
	elif           :
		#apply barrier profile 2
	else           :
		#apply barrier profile 3




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
		if resp.foundPath == 1
		 # transforms the pose coordinates to mapCoords
			path_pose = resp.path 
			path_mapCoord = [MapCoord()] * len(path_pose)
			for i, pose in enumerate(path_pose)
				path_mapCoord[i].x = path_pose[i].pose.position.x
				path_mapCoord[i].y = path_pose[i].pose.position.y
				path_mapCoord[i].map_id = 0
		# return path
			return path_mapCoord 
       except rospy.ServiceException, e:


def accessible_server():
    rospy.init_node('nav_link_server')
    s = rospy.Service('ApplyProfile', Apply_Profile, handle_ApplyProfile)
    print "Ready to revice requests."
    rospy.spin()

if __name__ == "__main__":
    nav_link_server()
