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
    return json.dumps(request.json)

run(host='localhost', port=18590) #should change to the port i chose earlier
