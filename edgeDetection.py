import argparse

import cv2

#get the image from command line arguments using argparser
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Path to the image')
args= vars(ap.parse_args())

image = cv2.imread(args['image'])

#covert the image in Gray scale
#remove the noise using Gausian filter
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)

#display both original and Blurred image after removal of Noise
cv2.imshow("Original",image)
cv2.imshow("blurred",blurred)

#Apply the Canny Edge Detection which will display the widden , tight and mid value versions
wide = cv2.Canny(blurred,10,150)
mid  = cv2.Canny(blurred,60,120)
tight = cv2.Canny(blurred,200,250)

cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)
