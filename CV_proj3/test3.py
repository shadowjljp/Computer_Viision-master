import cv2
import numpy as np
import os
import sys
#c: scalar
# [[c. 0. 0.]
#  [0. c. 0.]
#  [0. 0. 1.]]
#f:scalar
# [[1/f. 0. 0.]
#  [0. 1/f. 0.]
#  [0. 0. 1.]]
#u0 v0:shift
# [[  1.   0. -u0.]
#  [  0.   1.  v0.]
#  [  0.   0.   1.]]
#a b tilt
# [[ 1.     0.     0.   ]
#  [ 0.     1.     0.   ]
#  [-a  -b.     1.   ]]
#those result are u,v to X,Y
#result from X,Y to u,v should use inverse projection
def pointProject(src,f,u0,v0,a,b,c):
    #f,u0,v0,a,b,c = 1,0,0,0,0.001,1
    x = src[0]-u0
    y = src[1]-v0
    X = c*x/(f-a*x-b*y)
    Y = c*y/(f-a*x-b*y)
    return (X,Y)

# points1 = np.float32([ [30,30], [10,40], [40,10], [5,15] ])
# points2 = np.float32([ [0,0], [400,0], [0,400], [400,400] ])

# M = cv2.getPerspectiveTransform(points1, points2)
# print(M)
if len(sys.argv) != 8 :
    print(sys.argv[0], "takes 7 arguments. Not ", len(sys.argv)-1)
    sys.argv = [0 for i in range(8)]
    sys.exit(0)

f,u0,v0,a,b,c = [float(i) for i in sys.argv[2:8]]
M = np.float32([[f,0,u0],[0,f,-v0],[a,b,c]])

src = np.float32([[100, 100], [200, 100], [200, 200], [100, 200]])
p = []
for i in range(4):
    p.append(pointProject(src[i],float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7])))

dst = np.float32([p[0],p[1],p[2],p[3]])
print(dst)
print(src,"\n",dst)
M1 = cv2.getPerspectiveTransform(dst,src)
print(np.around(M, 5))
img = cv2.imread(sys.argv[1])
result = cv2.warpPerspective(img,M, (img.shape[1], img.shape[0]))#flags=cv2.WARP_INVERSE_MAP
cv2.namedWindow('gray1', cv2.WINDOW_AUTOSIZE)
cv2.imshow('gray1', img)
cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()