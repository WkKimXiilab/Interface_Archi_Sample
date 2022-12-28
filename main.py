import Interface
from define import Model, g_input_1, g_input_2, g_input_3

def run_inference(model_id):
    interface = Interface.Interface(model_id)

    print("input value : ", g_input_1)

    input_ret = interface.inputParsing(g_input_1)
    print("parsing : ", input_ret)

    infer_ret = interface.inference(input_ret)
    print("inference : ", infer_ret)

    output_ret = interface.outputParsing(infer_ret)
    print("generating : ", output_ret)

    print("test")

if __name__ == '__main__':
    run_inference(Model.SIMILARITY)
