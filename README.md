# Documentation
This file gives an overview of the project and explains how to use this repo to automatically detect objects in the
foreground of an image and remove the background.

## Project Setup for local testing in a docker container

1. Clone this repo to your local machine. ```git clone https://github.com/lenlehm/backgroundRemoval.git```  

1.1 Download the pre-trained U2-Net from [the authors](https://drive.google.com/file/d/1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ/view).
And if you're already on it [check out their original commit along with their research](https://github.com/NathanUA/U-2-Net)  
Create a folder names `saved_models` and load the previously downloaded model into that folder with the following structure `/saved_models/u2net/u2net.pth`

2. Install docker & Set up a docker container as described in the following two steps.

3. Run `docker build -t <your-image-name> .` in your terminal in the project directory.

4. Run `docker run -p 80:80 <your-image-name> .` in your terminal in the project directory.

5. Run `python model_request.py -p "path\\to\\your\\image.png"` for Windows or `python model_request.py -p "path/to/your/image.png"` on UNIX.

6. You should see the processed image. 

## Project Setup for usage in AWS EC2

1. Spin up an EC2 instance with at least a t2.medium hardware configuration (make sure to modify the security group to allow HTTP traffic on port 80 )

2. SSH into the running instance. 

3. Run `sudo yum install git` (optional for some more changes to come)
4. Run `sudo yum install docker`
5. Run `sudo service docker start`
6. Run `sudo usermod -a -G docker ec2-user`
7. Exit the instance and login again to make the changes work. 

8. Download the image from Docker Hub: `docker pull lenlehm/background-removal:v1`

9. Check whether the image is there: `docker images`

10. Run the container with the imageID you have seen from the previous command: `docker run -p 80:80 <your-imageID>`

11. Navigate to your public Ip Address of your instance: `your.public.IPv4.address:80'
You should not see something but you also shoudn't get an error if your instance is running.

12. Open the file `model_request.py` on your machine and change the endpoint to `your.public.IPv4.address:80/predict'

13. Run `python model_request.py -p "path/to/your/local/image.jpg"`
