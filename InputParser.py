from define import Model

from BaseDataConverter import BaseDataConverter

class InputParser(BaseDataConverter):
    def __init__(self, model):
        BaseDataConverter.__init__(self, model) 
    
    def _yolo(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'], 
            'roi_conv':input['roi_conv'],
            }

        return output

    def _retinaface(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'], 
            'retina_score':-1.0 
            }

        return output

    def _similarity(self, input):
        output = {
            'id':input['id'],
            'frame':input['frame'],
            'simila_score':-1
            }

        return output
