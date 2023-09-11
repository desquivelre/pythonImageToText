from PIL import Image
from argparse import ArgumentParser

import cv2
import imutils
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with the actual path to the Tesseract executable

argument_parser = ArgumentParser()
argument_parser.add_argument('-i', '--image', type=str, required=True, help='28-AGO-GNX.png')
arguments = vars(argument_parser.parse_args())

image = cv2.imread(arguments['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresholded = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imshow('Otsu', thresholded)
cv2.waitKey(0)

dist = cv2.distanceTransform(thresholded, cv2.DIST_L2, 5)
dist = cv2.normalize(dist,dist,0,1.0,cv2.NORM_MINMAX)
dist = (dist*255).astype('uint8')

cv2.imshow('Dist', dist)
cv2.waitKey(0)

dist = cv2.threshold(dist,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow('Dist Otsu', dist)
cv2.waitKey(0)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
# opening = cv2.morphologyEx(dist, cv2.MORPH_OPEN, kernel)
# cv2.imshow('Apertura', opening)
# cv2.waitKey(0)
#
# contours = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(contours)
#
# chars = []
# for contour in contours:
#     x,y,w,h = cv2.boundingRect(contour)
#     if w >= 35 and h >=100:
#         chars.append(contour)
#
# chars = np.vstack([chars[i] for i in range(0, len(chars))])
# hull = cv2.convexHull(chars)
#
# mask = np.zeros(image.shape[:2], dtype='uint8')
# cv2.drawContours(mask,[hull],-1,255,-1)
# mask = cv2.dilate(mask, None, iterations=2)
# cv2.imshow('Mascara', mask)
# cv2.waitKey(0)
#
# final = cv2.bitwise_and(opening, opening, mask=mask)

options = '-c tessedit_char_whitelist=qwertyuiopasdfghjklñzxcvbnm'
text = pytesseract.image_to_string(dist, config=options)
print(text)




# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# text = pytesseract.image_to_string(image)
# print(text)


# # Load an example image
# image = Image.open("28-AGO-GNX.png")
#
# # myconfig = r"--psm 3 --oem 3"
# myconfigg = '-c tessedit_char_whitelist=qwertyuiopasdfghjklñzxcvbnm'
#
# # Perform OCR on the image
# text = pytesseract.image_to_string(image, config='myconfig')
#
# print(text)