import json
from bottle import route, run, template, request, response
from bottle import get, post

@get('/')
def index():
    return '<b>Hello!</b> The accessibilitySLAM http-ros-link is functional!'

@post('/nav_xy_xy')
def navigate():
    j = request.json
    prof = j['profile']
    canStair = not prof['stairs']
    canHeavyDoor = not prof['heavy doors']
    start = j['start']
    goal = j['goal']

# ~~~~~~~~~~~~~~~~~~~ Point names, for convenience
    outdoors = (950,150)    #called A
    lounge = (850,450)      #called B
    lectureHall = (430,725) #called C
    # TODO: CALL ROS SERVICE HERE
    # TODO: returning hardcoded json for right now, 

# ~~~~~~~~~~~~~~~~~~~ Hardcoded Routes
    AB_00 =[ #can heavy doors & stairs
        outdoors,
        lounge
    ]
    AB_01=[#can heavy doors NO stairs
        outdoors,
        lounge
    ]
    AB_10 = [ #NO heavy doors, can stairs
        outdoors,
        lounge
    ]
    AB_11 = [ #NO heavy doors, NO stairs
        outdoors,
        lounge
    ]

    AC_00 =[ #heavy doors, can stairs
        outdoors,
        lectureHall
    ]
    AC_01 =[ #heavy doors, NO stairs
        outdoors,
        lectureHall
    ]
    AC_10 =[ #NO heavy doors, can stairs
        outdoors,
        lectureHall
    ]
    AC_11 =[ #NO heavy doors, NO stairs
        outdoors,
        lectureHall
    ]

    BC_00 =[ #heavy doors, can stairs
        lounge,
        lectureHall
    ]
    BC_01 =[ #heavy doors, NO stairs
        lounge,
        lectureHall
    ]
    BC_10 =[ #NO heavy doors, can stairs
        lounge,
        lectureHall
    ]
    BC_11 =[ #NO heavy doors, NO stairs
        lounge,
        lectureHall
    ]

    #~~~~~~~~~~~~~~~~~~~~~~~~~ Lookup relevant route & (maybe) reverse it
    #outdoors A
    #lounge B
    #lecturehall C

    if(canHeavyDoor and canStair):
        if(start['x']==outdoors[0] and start['y']==outdoors[1]):
            if(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = AB_00
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = AC_00
        elif(start['x']==lounge[0] and start['y']==lounge[1]):
            if(goal['x']==outdoors[0] and goal['y']==outdoors[1]):
                plan = AB_00[::-1]
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = BC_00
        elif(start['x']==lectureHall[0] and start['y']==lectureHall[1]):
            if(goal['x']==outdoors[0] and goal['y']==lectureHall[1]):
                plan = AC_00[::-1]
            elif(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = BC_00[::-1]

    if(canHeavyDoor and not canStair):
        if(start['x']==outdoors[0] and start['y']==outdoors[1]):
            if(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = AB_01
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = AC_01
        elif(start['x']==lounge[0] and start['y']==lounge[1]):
            if(goal['x']==outdoors[0] and goal['y']==outdoors[1]):
                plan = AB_01[::-1]
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = BC_01
        elif(start['x']==lectureHall[0] and start['y']==lectureHall[1]):
            if(goal['x']==outdoors[0] and goal['y']==lectureHall[1]):
                plan = AC_01[::-1]
            elif(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = BC_01[::-1]

    if(not canHeavyDoor and canStair):
        if(start['x']==outdoors[0] and start['y']==outdoors[1]):
            if(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = AB_10
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = AC_10
        elif(start['x']==lounge[0] and start['y']==lounge[1]):
            if(goal['x']==outdoors[0] and goal['y']==outdoors[1]):
                plan = AB_10[::-1]
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = BC_10
        elif(start['x']==lectureHall[0] and start['y']==lectureHall[1]):
            if(goal['x']==outdoors[0] and goal['y']==lectureHall[1]):
                plan = AC_10[::-1]
            elif(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = BC_10[::-1]

    if(not canHeavyDoor and not canStair):
        if(start['x']==outdoors[0] and start['y']==outdoors[1]):
            if(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = AB_11
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = AC_11
        elif(start['x']==lounge[0] and start['y']==lounge[1]):
            if(goal['x']==outdoors[0] and goal['y']==outdoors[1]):
                plan = AB_11[::-1]
            elif(goal['x']==lectureHall[0] and goal['y']==lectureHall[1]):
                plan = BC_11
        elif(start['x']==lectureHall[0] and start['y']==lectureHall[1]):
            if(goal['x']==outdoors[0] and goal['y']==lectureHall[1]):
                plan = AC_11[::-1]
            elif(goal['x']==lounge[0] and goal['y']==lounge[1]):
                plan = BC_11[::-1]

        #~~~~~~~~~~~~~~~~~~~~~~~~~ CONVERT TO DICT FOR json.dumps
    route = []
    for tup in plan:
        route.append({'x': tup[0], 'y': tup[1],'map_id': 1})
    return json.dumps({'plan': route})

# NORMALLY: run the server

run(host='localhost', port=18590)
