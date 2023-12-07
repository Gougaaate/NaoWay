import nao_driver
import time
import sys
from naoqi import ALProxy

import cv2
from detection import detect_yellow_ball

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

while (time.time() - t0) < 15:
    test_detection = True
    while not test_detection:
        motionProxy.moveTo(0,10,10)
        img_ok, cv_img, image_width, image_height = nao_drv.get_image()
        test_detection, _, _ = detect_yellow_ball(cv_img)
