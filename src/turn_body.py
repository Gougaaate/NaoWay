import nao_driver
# import nao_improc # python module for image processing
# import nao_ctrl # python module for robot control algorithms
import time
import sys
from naoqi import ALProxy

import cv2
import detection

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
    print
    "Could not create proxy to ALMotion"
    print
    "Error was: ", e

while (time.time() - t0) < 15:
    motionProxy.moveTo(0,0,10)