import numpy as np
import cv2

img = cv2.imread("input.jpg", cv2.IMREAD_UNCHANGED)

brightness = 100 #-127 to 127
contrast = 100 #-127 to 127

print("gamma =",(contrast/127+1) - contrast + brightness)

img = np.int16(img)
img = img * (contrast/127+1) - contrast + brightness
img = np.clip(img, 0, 255)
img = np.uint8(img)


cv2.imshow("water", img)
cv2.waitKey(0)
