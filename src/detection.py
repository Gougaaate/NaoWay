import sys
import motion
import time
from naoqi import ALProxy
import math

import cv2
import numpy as np


robotIp="172.20.26.29"
robotIp="betanao"
robotIp="172.20.11.241"
robotPort=9559

robotIp="localhost"
robotPort=11212

def detect_yellow_ball(image):
    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Apply a mask to the HSV image to get only yellow colors
    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    
    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour
    if contours:
        largest_contour = max(contours, key = cv2.contourArea)
        # Calculer la circularite
        perimeter = cv2.arcLength(largest_contour, True)
        area = cv2.contourArea(largest_contour)
        circularity = (4 * np.pi * area) / (perimeter ** 2)
        # Si l objet est suffisamment circulaire
        SEUIL_CIRCULARITE = 0.7
        if circularity > SEUIL_CIRCULARITE:
            print("Objet detecte !")
            # Calculer les moments pour le barycentre
            moments = cv2.moments(largest_contour)
            if moments["m00"] != 0:
                x_g = int(moments["m10"] / moments["m00"])
                y_g = int(moments["m01"] / moments["m00"])
            else:
                x_g, y_g = 0, 0

            # Dessiner un cercle autour de l objet
            cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
            cv2.circle(image, (x_g, y_g), 5, (0, 255, 0), -1)
            # Afficher le barycentre
            cv2.putText(image, "barycentre", (x_g - 20, y_g - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print("Barycentre : ({}, {})".format(x_g, y_g))
            
            return True, (x_g, y_g), cv2.contourArea(largest_contour)
        
    # Afficher l image avec les contours detectes
    cv2.imshow("Image avec contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return False, None, None

if __name__ == "__main__":
    # path_to_image = "../../../imgs/naosimimgs/IMG_8589.JPG"
    path_to_image = "../../../imgs/naosimimgs/naosimimg_0130.png"
    image = cv2.imread(path_to_image)
    detect_yellow_ball(image)
    

