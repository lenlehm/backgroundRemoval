import numpy as np
from flask import Flask, request
import torch
from model.u2net import U2NET
import os
from u2_net_API import u2net_api_call

model = None
app = Flask(__name__)

def load_neural_net(model_dir):
    """
    Function to load the neural network only once, when the app is started.
    """
    global model
    print("...load U2NET---173.6 MB")
    model = U2NET(3, 1)
    model.load_state_dict(torch.load(model_dir, map_location=torch.device('cpu')))
    model.eval()

@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    """
    Currently only supports one sample as input. Also at the function expects the data in the json format representing
    the image to be a numpy array.
    """
    if request.method == 'POST':
        data_dict = request.get_json()  # Get data posted as a json
        image_list = data_dict["image"]
        image_np = np.array(image_list)
        rem_background_img = u2net_api_call(image_np, model)
        image_json = {"image": rem_background_img.tolist()}

    return image_json


if __name__ == '__main__':
    model_name = 'u2net'
    model_dir = os.path.join(os.getcwd(), 'saved_models', model_name, model_name + '.pth')

    load_neural_net(model_dir)  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)