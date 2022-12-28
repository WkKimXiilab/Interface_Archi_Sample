from define import Model
from abc import * 

class BaseDataConverter(metaclass=ABCMeta) :
    def __init__(self, model):
        if(model == Model.YOLO):
            self._select_function = self._yolo
        elif(model == Model.RETINAFACE):
            self._select_function = self._retinaface
        elif(model == Model.SIMILARITY):
            self._select_function = self._similarity
        elif(model == Model.HELMET):
            self._select_function = self._similarity

    def Convert(self, input):
        return self._select_function(input)

    @abstractmethod
    def _yolo(self, input):
        pass

    @abstractmethod
    def _retinaface(self, input):
        pass

    @abstractmethod
    def _similarity(self, input):
        pass
    