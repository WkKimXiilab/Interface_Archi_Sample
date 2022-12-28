from enum import Enum

g_input_1 = {
    'id':1,
    'frame':"1920*1080",
    'roi':(-1, -1, -1, -1),
    'retina_score':-1.0, 
    'simila_score':-1
}

g_input_2 = {
    'id':2,
    'frame':"1280*720",
    'roi':(-1, -1, -1, -1),
    'retina_score':-1.0, 
    'simila_score':-1
}

g_input_3 = {
    'id':3,
    'frame':"960*540",
    'roi':(-1, -1, -1, -1),
    'retina_score':-1.0, 
    'simila_score':-1
}

class Model(Enum):
    YOLO = 1
    RETINAFACE = 2
    SIMILARITY = 3
    HELMET = 4