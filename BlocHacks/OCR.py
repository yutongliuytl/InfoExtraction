import pytesseract
import cv2
import numpy as np

from PIL import Image

def OCR(filename):

    kernel = np.ones((3,3),np.uint8)

    image = cv2.imread(filename, 0)

    image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,15)

    # cv2.imshow('', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(image)

    file = open("data.txt", 'w')
    file.writelines(text)
