import cv2
import numpy as np
from time import sleep

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.threshold(img, 135, 225, cv2.THRESH_BINARY)[1]
print(img.shape)
img = cv2.resize(img, (203*2, 261*2))
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 0.4
color = (0, 0, 0)
thickness = 1


resImg = np.ones((261*2, 203*2, 1), np.uint8)*255

for i in range(261*2):
    for j in range(203*2):
        if (img[i, j] == 0 and i % 5 == 0 and j % 5 == 0):
            resImg = cv2.putText(resImg, 'Tri', (j, i), font,
                                 fontScale, color, thickness, cv2.LINE_AA)
            cv2.imshow("Thay Tri", resImg)
            cv2.waitKey(1)


resImg = cv2.cvtColor(resImg, cv2.COLOR_GRAY2RGB)
s = "Send a sincere thanks"
p = [50, 450]
color = (0, 225, 0)
fontScale = 0.6
for c in s:
    p[0] += 14
    resImg = cv2.putText(resImg, c, tuple(p), font,
                         fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Thay Tri", resImg)
    cv2.waitKey(50)


s = "Teacher Minh Tri"
p = [80, 480]
color = (225, 0, 0)
fontScale = 0.6
for c in s:
    p[0] += 14
    resImg = cv2.putText(resImg, c, tuple(p), font,
                         fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Thay Tri", resImg)
    cv2.waitKey(delay=100)

cv2.waitKey()
