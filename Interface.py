import OutputParser
import Inference
import InputParser

class Interface:
    def __init__(self, model):
        print("this is Interface!")
        
        self.__inputParser = InputParser.InputParser(model) 
        self.__inference = Inference.Inference(model) 
        self.__outputParser = OutputParser.OutputParser(model)

    def inputParsing(self, value):
        return self.__inputParser.Convert(value)
    
    def inference(self, value):
        return self.__inference.Convert(value)

    def outputParsing(self, value):
        return self.__outputParser.Convert(value)

