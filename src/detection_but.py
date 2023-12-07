import cv2
import numpy as np


def detect_red_goal(image):
    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range of red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    # Create a mask to filter out red colors
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Define range of red color (wrap-around hue values)
    # lower_red = np.array([160, 100, 100])
    # upper_red = np.array([180, 255, 255])

    # Create a second mask for wrap-around hue values
    # mask2 = cv2.inRange(hsv_image, lower_red, upper_red)

    # Combine masks to get the final mask
    # mask = cv2.bitwise_or(mask1, mask2)
    
    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour
    if contours:
        return True
        
    else:
        return False



# if __name__ == "__main__":
#     path_to_image = "../../../imgs/naosimimgs/naosimimg_0000.png"
#     image = cv2.imread(path_to_image)
#     detect_red_goal(image)

    

