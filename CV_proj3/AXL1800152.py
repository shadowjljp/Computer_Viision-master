import math

import cv2
import numpy as np
import sys

# read arguments
from cv2.cv2 import cvtColor

if (len(sys.argv) != 3):
    print(sys.argv[0], ": takes 2 arguments. Not ", len(sys.argv) - 1)
    print("Example:", sys.argv[0], "scenary.jpg 1 ")
    sys.exit()

name_input = sys.argv[1]
c = float(sys.argv[2])

inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)

# M=np.zeros([3,3],dtype=np.uint8)
# M[2]=c(u-u0)
rows, cols, band = inputImage.shape

inputImage2 = np.copy(inputImage)


def perspectiveTransform_M1():
    # pts1 = np.float32([[rows * 0.25, cols * 0.25], [rows * 0.75, cols * 0.25], [rows * 0.25, cols * 0.75],
    #                   [rows * 0.75, cols * 0.75]])
    pts1 = np.float32([[0, 0], [100, 0], [100, 100], [0, 100]])
    X0 = []
    Y0 = []
    for i in range(4):
        X0.append((c * (pts1[i][0] - 0)) / (1 - (-0.001) * (pts1[i][0] - 0) - 0 * (pts1[i][1] - 0)))
        Y0.append((c * (pts1[i][1]) - 0) / (1 - (-0.001) * (pts1[i][0] - 0) - 0 * (pts1[i][1] - 0)))
    # print(X0)
    pts2 = np.float32([[X0[0], Y0[0]], [X0[1], Y0[1]], [X0[2], Y0[2]], [X0[3], Y0[3]]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    print('M= ', M)
    return M

def perspectiveTransform_M2():
    # pts1 = np.float32([[rows * 0.25, cols * 0.25], [rows * 0.75, cols * 0.25], [rows * 0.25, cols * 0.75],
    #                   [rows * 0.75, cols * 0.75]])
    pts1 = np.float32([[0, 0], [100, 0], [100, 100], [0, 100]])
    X0 = []
    Y0 = []
    for i in range(4):
        X0.append((c * (pts1[i][0] - 0)) / (1 - 0 * (pts1[i][0] - 0) - 0.0009 * (pts1[i][1] - 0)))
        Y0.append((c * (pts1[i][1]) - 0) / (1 - 0 * (pts1[i][0] - 0) - 0.0009 * (pts1[i][1] - 0)))
    # print(X0)
    pts2 = np.float32([[X0[0], Y0[0]], [X0[1], Y0[1]], [X0[2], Y0[2]], [X0[3], Y0[3]]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    print('M= ', M)
    return M


M1 = perspectiveTransform_M1()
inputImage = cv2.warpPerspective(inputImage, M1, (inputImage.shape[1], inputImage.shape[0]))
# For Vertical
M2 = perspectiveTransform_M2()

inputImage2 = cv2.warpPerspective(inputImage, M2, (inputImage2.shape[1], inputImage2.shape[0]))

cv2.imshow("Vertical tilt", inputImage)
cv2.imshow("Horizontal tilt", inputImage2)

cv2.waitKey(0)
cv2.destroyAllWindows()
