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
    canStair = prof['CanStair']
    canHeavyDoor = prof['CanHeavyDoor']
    start = j['Start']
    goal = j['Goal']

    outdoors = (950,150)
    lounge = (850,450)
    lectureHall = (430,725)
    # TODO: CALL ROS SERVICE HERE
    # TODO: returning json as string for right now, 
    # return the route in the future instead
    # returning a fake route first instead
    navcords = [
        [ #start point 0
            [ #end point 1
                [#can stairs
                    [#can heavy doors
                        [ #points in order of traversal as tuples
                            outdoors,
                            lounge
                        ],
                        [ #points in order of traversal as tuples
                            outdoors,
                            lounge
                        ]
                    ],
                    [#can heavy doors
                        [ #points in order of traversal as tuples
                            outdoors,
                            lounge
                        ],
                        [ #points in order of traversal as tuples
                            outdoors,
                            lounge
                        ]
                    ]
                ]
            ],
            [#end point 2

            ]
        ],
        [ #start point 1
            [ #end point 2
                [#can stairs
                    [#can heavy doors
                        [ #points in order of traversal as tuples
                            lounge,
                            lectureHall
                        ],
                        [ #points in order of traversal as tuples
                            lounge,
                            lectureHall
                        ]
                    ],
                    [#can heavy doors
                        [ #points in order of traversal as tuples
                            lounge,
                            lectureHall
                        ],
                        [ #points in order of traversal as tuples
                            lounge,
                            lectureHall
                        ]
                    ]
                ]
            ],
            [#end point 0

            ]
        ],
        [ #start point 2
            [ #end point 0
                [#can stairs
                    [#can heavy doors
                        [ #points in order of traversal as tuples
                            lectureHall,
                            outdoors
                        ],
                        [ #points in order of traversal as tuples
                            lectureHall,
                            outdoors
                        ]
                    ],
                    [#can heavy doors
                        [ #points in order of traversal as tuples
                            lectureHall,
                            outdoors
                        ],
                        [ #points in order of traversal as tuples
                            lectureHall,
                            outdoors
                        ]
                    ]
                ]
            ],
            [#end point 1

            ]
        ]
    navcords[0][1][: for i in 0..1][for j in 0...1] = navcords[1][0][i][j][::-1]
    navcords[1][1][: for i in 0..1][for j in 0...1] = navcords[2][0][i][j][::-1]
    navcords[2][1][: for i in 0..1][for j in 0...1] = navcords[0][0][i][j][::-1]

    plan = []
    for tup in navcords[start][goal][canStair][canHeavyDoor]:
        plan.append(retdict{'x': tup[0], 'y': tup[1],'map_id': 1})
    
    retdict = {'plan': plan}
    return json.dumps(retdict)

run(host='localhost', port=18590) #should change to the port i chose earlier
