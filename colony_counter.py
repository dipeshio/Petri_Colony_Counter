import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pillow_heif import register_heif_opener
import os


register_heif_opener()
print(f'')

def select_img():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def file_format():
    d1 ='G:/My Drive/Bucknell Summer 24/Summer 2024/Personal Project/Colony Counter/Plates'
    d2 ='G:/My Drive/Bucknell Summer 24/Summer 2024/Personal Project/Colony Counter/plates_converted/'
    count = 0
    dir = os.fsencode(d1)
    ## looping over files in directory for file conversion
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        count = count + 1
        if filename.endswith(".HEIC") or filename.endswith(".png"):
            img = Image.open('G:/My Drive/Bucknell Summer 24/Summer 2024/Personal Project/Colony Counter/Plates/' + filename)
            img.save(f'{d2}COLONY_{count}.jpg')
            continue
        else:
            continue
    return d1 and d2

def circle_outline():
    img = cv2.imread('G:/My Drive/Bucknell Summer 24/Summer 2024/Personal Project/Colony Counter/plates_converted/COLONY_N.jpg')
    img = cv2.resize(img, (600 , 800))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.medianBlur(gray, 25)  # cv2.bilateralFilter(gray,10,50,50)

    minDist = 100
    param1 = 30  # 500
    param2 = 50  # 200 #smaller value-> more false circles
    minRadius = 5
    maxRadius = 100  # 10

    # docstring of HoughCircles: HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2,
                               minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

    # Show result for testing:
    cv2.imshow('img', )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    d2 ='G:/My Drive/Bucknell Summer 24/Summer 2024/Personal Project/Colony Counter/plates_converted/'
    circle_outline()

main()