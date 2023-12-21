import cv2
import numpy as np

def grayman(img, threshold_value=128):
    # グレースケールに変換
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 二値化
    _, thresholded_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

    return thresholded_img