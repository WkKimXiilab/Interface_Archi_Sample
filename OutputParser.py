from define import Model

from BaseDataConverter import BaseDataConverter

class OutputParser(BaseDataConverter):
    def __init__(self, model):
        BaseDataConverter.__init__(self, model) 
    
    def _yolo(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'], 
            'roi':input['roi'],
            'retina_score':-1.0, 
            'simila_score':-1
            }

        return output

    def _retinaface(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'], 
            'roi':(-1, -1, -1, -1),
            'retina_score':input['retina_score'], 
            'simila_score':-1
            }
        
        return output

    def _similarity(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'],
            'roi':(-1, -1, -1, -1),
            'retina_score':-1.0, 
            'simila_score':input['simila_score'], 
            }
        
        return output
