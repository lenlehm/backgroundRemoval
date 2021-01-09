import argparse
import requests
from skimage import io
import matplotlib.pyplot as plt

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
    help="specify the path/to/your/image.jpeg")
args = vars(ap.parse_args())


def visualize_img(img, description_string="", x_label="", y_label=""):
    plt.figure()
    plt.title(description_string)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.gray()
    plt.imshow(img)
    plt.show()

def send_request(image):
    url = 'http://localhost:80/predict' # if flask backend runs locally
    # url = 'http://ec2-3-126-116-182.eu-central-1.compute.amazonaws.com:80/predict' # if flask backend runs on AWS
    image_json = {"image":image.tolist()}
    r = requests.post(url,json=image_json)
    r_dict = r.json()
    rem_background_img = r_dict["image"]

    visualize_img(rem_background_img, description_string="removed background")

if __name__=="__main__":
    test_img_path = args["path"]
    input_image = io.imread(test_img_path)  # <class 'numpy.ndarray'>
    send_request(input_image)