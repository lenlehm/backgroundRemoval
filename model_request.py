import requests
from skimage import io
from helpers import visualize_img

def send_request(image):
    url = 'http://localhost:80/predict' # if flask backend runs locally
    # url = 'http://ec2-3-126-116-182.eu-central-1.compute.amazonaws.com:80/predict' # if flask backend runs on AWS
    image_json = {"image":image.tolist()}
    r = requests.post(url,json=image_json)
    r_dict = r.json()
    rem_background_img = r_dict["image"]

    visualize_img(rem_background_img, description_string="removed background")

if __name__=="__main__":
    test_img_path = "/Users/felixasanger/Desktop/background_removal/test_data/test_images/J306P12B__20201116_22-25-33__c0.jpg"
    input_image = io.imread(test_img_path)  # <class 'numpy.ndarray'>
    send_request(input_image)