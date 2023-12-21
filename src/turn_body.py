import nao_driver
import time
import sys
from naoqi import ALProxy

import cv2
from detection import detect_yellow_ball
from detection import distance_to_ball
from detection_but import detect_red_goal

alpha = 289.9591996480879
ball_diam = 0.09
cam_height = 0.4

robot_ip = "localhost"
robot_port = 11212
if (len(sys.argv) >= 2):
    robot_ip = sys.argv[1]
if (len(sys.argv) >= 3):
    robot_port = int(sys.argv[2])
    
nao_drv = nao_driver.NaoDriver(nao_ip=robot_ip, nao_port=robot_port)
if nao_drv.vnao:
    nao_drv.set_virtual_camera_path("../../../imgs")
nao_drv.set_nao_at_rest()
cam_num = 0
nao_drv.change_camera(cam_num)
nao_drv.show_image(key=3000)  # 3 s


t0 = time.time()
try:
    motionProxy = ALProxy("ALMotion", robot_ip, robot_port)
except Exception, e:
    print "Could not create proxy to ALMotion"
    print "Error was: ", e

# while (time.time() - t0) < 15:
    # test_detection = False
img_ok, cv_img, image_width, image_height = nao_drv.get_image()
test_detection, _, area = detect_yellow_ball(cv_img)


while not test_detection:
    motionProxy.moveTo(0,0,1)
    img_ok, cv_img, image_width, image_height = nao_drv.get_image()
    test_detection, _, area = detect_yellow_ball(cv_img)
    # print test_detection

distance = distance_to_ball(area, alpha, cam_height, ball_diam)

while distance > 1 :
    motionProxy.moveTo(0.5,0,0)
    _, cv_img, _, _ = nao_drv.get_image()  
    test_detection, _, area = detect_yellow_ball(cv_img)
    if not test_detection:
        motionProxy.moveTo(-0.2,0,0)
        break
    distance = distance_to_ball(area, alpha, cam_height, ball_diam)






# while the robot does not detect the red goal, it moves around the ball
while not detect_red_goal(cv_img):
    motionProxy.moveTo(0,0.3,-0.25)
    img_ok, cv_img, image_width, image_height = nao_drv.get_image()
    print detect_red_goal(cv_img)
    # print test_detection
    
# while True :
#     img_ok, cv_img, image_width, image_height = nao_drv.get_image()
#     test_detection, _, area = detect_yellow_ball(cv_img)
#     distance_to_ball(area, alpha, cam_height, ball_diam)
#     test_detection, _, area = detect_yellow_ball(cv_img)
#     motionProxy.moveTo(0,0.9/2,-1/2)
    
    # detect_red_goal(cv_img)
    # print detect_red_goal(cv_img)

# motionProxy.moveTo(0,0.9,-0.9)
motionProxy.moveTo(0,0.6,-0.6)
motionProxy.moveTo(0,1,0)
motionProxy.moveTo(30,-5,0)
