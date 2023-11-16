import cv2
import numpy as np

img_60 = cv2.imread("../img/img60.png")
img_80 = cv2.imread("../img/img80.png")
img_100 = cv2.imread("../img/img100.png")
img_120 = cv2.imread("../img/img120.png")


def compute_distance(*args):

    lower_yellow = np.array([0, 130, 130])
    upper_yellow = np.array([40, 255, 255])

    list_db = [np.sqrt(0.60 ** 2 + 0.40 ** 2), np.sqrt(0.80 ** 2 + 0.40 ** 2), np.sqrt(1.0 ** 2 + 0.40 ** 2),
               np.sqrt(1.20 ** 2 + 0.40 ** 2)]

    contours_list = []
    pixel_length_list = []

    for img in args:
        hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_list.append(contours)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            largest_contour_area = cv2.contourArea(largest_contour)
            pixel_length = np.sqrt(4 * largest_contour_area / np.pi)
            pixel_length_list.append(pixel_length)

    k = 0
    for img, contours in zip(args, contours_list):
        cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
        k += 1
        cv2.imshow("test", img)
        cv2.waitKey(0)

    alpha = 0
    for k in range(len(contours_list)):
        alpha += list_db[k] * pixel_length_list[k] / 0.09
    alpha = alpha / len(contours_list)
    print(f"alpha = {alpha}")
    return alpha


if __name__ == '__main__':
    compute_distance(img_60, img_80, img_100, img_120)
