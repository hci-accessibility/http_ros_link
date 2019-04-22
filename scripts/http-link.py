import json
from bottle import route, run, template, request, response
from bottle import get, post
import rospy
from accessible_navigator.srv import *
from accessible_navigator.msg import *
@get('/')
def index():
    return '<b>Hello!</b> The accessibilitySLAM http-ros-link is functional!'

@post('/nav_xy_xy')
def navigate():
    j = request.json
    prof = j['Profile']
    start = j['Start']
    goal = j['Goal']
    # TODO: CALL ROS SERVICE HERE
    # TODO: returning json as string for right now, 
    # return the route in the future instead
    return json.dumps(request.json)


if __name__ == '__main__':
	print("Waiting for nav_xy_xy service on accessible_nav_server ROS node...")
	rospy.wait_for_service('accessible_nav_server')
	print("accessible_nav_server ROS node found. Waiting for HTTP requests...")
	run(host='localhost', port=18590)