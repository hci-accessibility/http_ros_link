import json
from bottle import route, run, template, request, response
from bottle import get, post

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
    # returning a fake route first instead
    retdict = {
	'plan': [
		{'x': 1, 'y': 1, 'map_id': 1},
		{'x': 10, 'y': 1, 'map_id': 1},
		{'x': 10, 'y': 10, 'map_id': 1},
		{'x': 100, 'y':100, 'map_id': 1},
		{'x': 100, 'y':1000, 'map_id': 1},
		{'x': 1000, 'y':900, 'map_id': 1}
		]
	}
    return json.dumps(retdict)

run(host='localhost', port=18590) #should change to the port i chose earlier
