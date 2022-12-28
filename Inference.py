from define import Model

from BaseDataConverter import BaseDataConverter

class Inference(BaseDataConverter):
    def __init__(self, model):
        BaseDataConverter.__init__(self, model) 
    
    def _yolo(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'], 
            'roi':(50, 50, 100, 100) 
            }

        return output

    def _retinaface(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'], 
            'retina_score':0.50 
            }
        
        return output

    def _similarity(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'],
            'simila_score':50
            }
        
        return output
