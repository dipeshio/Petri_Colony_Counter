import cv2
import numpy as np
from tkinter.filedialog import askopenfilename
import cv2 as cv


def create_circle():
    img = cv.imread(askopenfilename())
    img = cv.resize(img, (700, 900))
    print(f'Pre-crop dimensions: {img.shape}')
    img = img[250:610, 150:510]  ## assumption that all of the imaees are the same size
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(img,5)
    #img = cv.resize(gray, (700, 900))


    ## creating a roi with cropped image

## detecting circles in picture

    rows = gray.shape[0]
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, rows * 8, param1=100, param2=30, minRadius=0, maxRadius=400)

 ## drawing out the circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(img, center, radius, (255, 0, 255), 3)
    img_source = 'Source'
    cv.namedWindow(img_source)
    cv.imshow(img_source, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

## scaling issue --> need to make all image size the same

def scale_crop():
    img = cv.imread(askopenfilename())
    img = cv.resize(img, (700, 900))
    #print(f'Pre-crop dimensions: {img.shape}')
    #crop = img[250:610, 150:510] ## assumption that all of the imaees are the same size
    ## resize happens beforehand to 700x900
    ## ideal dims: [350 x 360], maybe keep it a square?
    #print(f'Post-crop dimensions: {crop.shape}')
    cv2.waitKey(0)
    cv.destroyAllWindows()


scale_crop()
def main():
    create_circle()
