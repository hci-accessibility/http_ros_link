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
    cantStair = True if prof['stairs'] == "true" else False
    cantHeavyDoor = True if prof['heavy doors']== "true" else False
    print("cantStair: %s cantHeavyDoor: %s" % (cantStair, cantHeavyDoor))
    start = j['start']
    goal = j['goal']

# ~~~~~~~~~~~~~~~~~~~ Point names, for convenience
    #~~~~ Names used as starts or destinations
    outdoors = (950,150)    #called A
    lounge = (850,450)      #called B
    lectureHall = (430,725) #called C
    #~~~~ Names used for purely convenience points
    outNW = (9 , 19)
    outNE = (971 , 13)
    outSE = (925 , 969)
    outSW = (37 , 997)
    inNW = (267 , 257)
    inNE = (690 , 258)
    inSE = (687 , 649)
    inSW = (261 , 584)
    loungeDoorNout = (695 , 375)
    loungeDoorNin = (817 , 375)
    loungeDoorSout = (703 , 575)
    loungeDoorSin = (839 , 575)
    LS1 = (360 , 685)
    LS2 = (430 , 700)
    LS3 = (541 , 700)
    LS4 = (623 , 679)
    LS5 = (567 , 931)
    LS6 = (546 , 785)
    LS7 = (702 , 893)
    lectSW = (365 , 590)
    lectSE = (613 , 667)
    rampBot = (291 , 671)
    rampTop = (170 , 950)
    N = (467 , 5)
    S = (475 , 1050)
    E = (953 , 455)
    W = (5 , 500)
    stairsNEtop = (830 , 155)
    stairsSEtop = (859 , 818)
    stairsNWtop = (105 , 121)
    outNES = (957 , 174)
    outSEN = (959 , 782)
    outSES = (759 , 1034)
    outNEN = (798 , 4)
    outNWN = (178 , 7)
    outSWS = (206 , 1038)
    foyer = (514 , 967)



    # TODO: CALL ROS SERVICE HERE
    # TODO: returning hardcoded json for right now, 

# ~~~~~~~~~~~~~~~~~~~ Hardcoded Routes
 # 00 = neither constraint
 # 01 = stairs constrained
 # 10 = heavy doors constrained
 # 11 = both constraints
    AB_00 =[ #can heavy doors & stairs
        outdoors,
        stairsNEtop,
        inNE,
        loungeDoorNout,
        loungeDoorNin,
        lounge
    ]
    AB_01=[#can heavy doors NO stairs
        outdoors,
        outNES,
        outSEN,
        outSE,
        outSES,
        S,
        outSWS,
        rampTop,
        rampBot,
        inSW,
        inNW,
        inNE,
        loungeDoorNout,
        loungeDoorNin,
        lounge
    ]
    AB_10 = [ #NO heavy doors, can stairs
        outdoors,
        outNES,
        outSEN,
        stairsSEtop,
        inSE,
        loungeDoorNout,
        loungeDoorNin,
        lounge
    ]
    AB_11 = AB_01 #NO heavy doors, NO stairs, SAME as AB_01 because not cutting thru lecture hall.

    AC_00 =[ #can heavy doors, can stairs
        outdoors,
        stairsNEtop,
        inNE,
        loungeDoorSout,
        lectSW,
        LS4,
        LS3,
        LS6,
        lectureHall
    ]
    AC_01 =[ #can heavy doors, NO stairs
        outdoors,
        outNES,
        outSEN,
        outSE,
        outSES,
        S,
        foyer,
        LS5,
        LS6,
        lectureHall
    ]
    AC_10 =[ #NO heavy doors, can stairs
        outdoors,
        outNEN,
        outNWN,
        stairsNWtop,
        inNW,
        inSW,
        lectSW,
        LS1,
        LS2,
        LS3,
        LS6,
        lectureHall
    ]
    AC_11 =[ #NO heavy doors, NO stairs
        outdoors,
        outNES,
        outSEN,
        outSE,
        outSES,
        S,
        outSWS,
        rampTop,
        rampBot,
        inSW,
        lectSW,
        LS1,
        LS2,
        LS3,
        LS6,
        lectureHall
    ]

    BC_00 =[ #can heavy doors, can stairs
        lounge,
        loungeDoorNin,
        loungeDoorNout,
        loungeDoorSout,
        lectSE,
        LS4,
        LS3,
        LS6,
        lectureHall
    ]
    BC_01 = BC_00 #can heavy doors, NO stairs #SAME as BC_00 b/c BC_00 route involves no stairs
        
    BC_10 =[ #NO heavy doors, can stairs
        lounge,
        loungeDoorNin,
        loungeDoorNout,
        inNE,
        inNW,
        inSW,
        lectSW,
        LS1,
        LS2,
        LS3,
        LS6,
        lectureHall
    ]
    BC_11 = BC_10 #NO heavy doors, NO stairs #SAME as BC_10 b/c BC_10 route involves no stairs
        

    #~~~~~~~~~~~~~~~~~~~~~~~~~ Lookup relevant route & (maybe) reverse it
    #outdoors A
    #lounge B
    #lecturehall C

    if(cantHeavyDoor and cantStair):
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

    if(not cantHeavyDoor and cantStair):
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

    if(cantHeavyDoor and not cantStair):
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

    if(not cantHeavyDoor and not cantStair):
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

        #~~~~~~~~~~~~~~~~~~~~~~~~~ CONVERT TO DICT FOR json.dumps
    route = []
    for tup in plan:
        route.append({'x': tup[0], 'y': tup[1],'map_id': 1})
    return json.dumps({'plan': route})

# NORMALLY: run the server

run(host='localhost', port=18590)
