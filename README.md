# Documentation
This file gives an overview of the project and explains how to use this repo to automatically detect objects in the
foreground of an image and remove the background.

## Project Setup for local testing in a docker container

1. Clone this repo to your local machine. 
1.1 Download the pre-trained U2-Net from [the authors](https://drive.google.com/file/d/1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ/view).
And if you're already on it [check out their original commit along with their research](https://github.com/NathanUA/U-2-Net)

2. Set up a docker container as described in the following two steps.

3. Run `docker build -t <your-image-name> .` in your terminal in the project directory.

4. Run `docker run -p 80:80 <your-image-name> .` in your terminal in the project directory.

5. Open the file model_request.py` and modify the variable `test_img_path` such that it contains the path to the image you want to process.

6. Run `python model_request.py`

7. You should see the processed image. 

## Project Setup for usage in AWS EC2

1. Spin up an EC2 instance with at least a t2.medium hardware configuration (make sure to modify the security group to allow HTTP traffic on port 80 )

2. SSH into the running instance. 

3. Run `sudo amazon-linux-extras install docker`
4. Run `sudo yum install docker`
5. Run `sudo service docker start`
6. Run `sudo usermod -a -G docker ec2-user`

7. Exit the instance and login again to make the changes work. 

8. Run `docker build -t <your-image-name> .` on the running instance.

9. Run `docker run -p 80:80 <your-image-name> .` on the running instance.

10. Open another terminal on your local machine and run `python model_request.py` (make sure that line 7 is not commented and contains the correct instance public-dns-name)
