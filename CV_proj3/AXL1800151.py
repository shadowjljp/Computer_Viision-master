import math

import cv2
import numpy as np
import sys

# read arguments
from cv2.cv2 import cvtColor

if (len(sys.argv) != 8):
    print(sys.argv[0], ": takes 7 arguments. Not ", len(sys.argv) - 1)
    print("Example:", sys.argv[0], "fruits.jpg 0 0.001 1 1 0 0 ")
    sys.exit()

name_input = sys.argv[1]
f = float(sys.argv[2])
u0 = float(sys.argv[3])
v0 = float(sys.argv[4])
a = float(sys.argv[5])
b = float(sys.argv[6])
c = float(sys.argv[7])

inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)

# M=np.zeros([3,3],dtype=np.uint8)
# M[2]=c(u-u0)
rows, cols, band = inputImage.shape


def perspectiveTransform():
    # pts1 = np.float32([[rows * 0.25, cols * 0.25], [rows * 0.75, cols * 0.25], [rows * 0.25, cols * 0.75],
    #                   [rows * 0.75, cols * 0.75]])
    pts1 = np.float32([[0, 0], [100, 0], [100, 100], [0, 100]])
    X0 = []
    Y0 = []
    for i in range(4):
        X0.append((c * (pts1[i][0] - u0)) / (f - a * (pts1[i][0] - u0) - b * (pts1[i][1] - v0)))
        Y0.append((c * (pts1[i][1]) - v0) / (f - a * (pts1[i][0] - u0) - b * (pts1[i][1] - v0)))
    # print(X0)
    pts2 = np.float32([[X0[0], Y0[0]], [X0[1], Y0[1]], [X0[2], Y0[2]], [X0[3], Y0[3]]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    print('M= ', M)
    return M


M = perspectiveTransform()
inputImage = cv2.warpPerspective(inputImage, M, (inputImage.shape[1], inputImage.shape[0]))

cv2.imshow("Perspective projection", inputImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
