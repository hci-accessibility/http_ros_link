#from                 import *
import rospy

def handle_Navigate_XY(req):
	handle_Apply_Profile()
	#convert MapCoord into RTABMAP coordinates
	#getPath()
	getPath()


def handle_Navigate_Room(req):
	handle_Apply_Profile()
	MapCoord end = look_up_room_coordinates(req.goal_building, req.goal_room)

	std_msgs/bool goal_clear = handle_CheckClear_XY(end)

	if goal_clear == True
		MapCoord start = look_up_room_coordinates(req.start_building, req.start_room)
		handle_Navigate_XY(start, end)
	else 


def handle_Navigate_XYR(req):
	handle_Apply_Profile()
	MapCoord end = look_up_room_coordinates(req.goal_building, req.goal_room)
	handle_Navigate_XY(req.start, end)

def handle_Navigate_RXY(req):
	MapCoord start = look_up_room_coordinates(req.start_building, req.start_room)
	handle_Navigate_XY(start, req.end)

def handle_CheckClear_XY(req):
	# 

def handle_Apply_Profile(req):


def getPath()


def look_up_room_coordinates(building_id, room_id):
	# look up Room X/Y from database,
	# store X/Y in coord,
	MapCoord coord
	#coord.point.x = 
	#coord.point.y = 		
	#coord.map_id =
	#return coord
	return coord
	


def add_Navigate_server():
	rospy.init_node('navigate_server')
	service_room = rospy.Service('navigate_room', Navigate_Room, handle_Navigate_Room)
	service_xy = rospy.Service('navigate_xy', Navigate_XY, handle_Navigate_XY)
	service_xyr = rospy.Service('navigate_xyr', Navigate_XYR, handle_Navigate_XYR)
	service_rxy = rospy.Service('navigate_rxy', Navigate_RXY, handle_Navigate_RXY)
	service_CheckClear_XY = rospy.Service('checkclear_xy', CheckClear_XY, handle_CheckClear_XY)
	service_apply_profile = rospy.Service('apply_profile', Apply_Profile, handle_Apply_Profile)
	print("Services Registered.")
	rospy.spin()

if __name == "__main__":
	add_Navigate_server()
