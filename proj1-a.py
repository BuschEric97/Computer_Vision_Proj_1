# CS4391.001 - Project 1
#
# This file is the program
# for part 1 of project 1
#
# Program by: Eric Busch
# edb160230@utdallas.edu

import cv2
import numpy as np
import sys
import convertColors

# get and assign command line arguments
if (len(sys.argv) != 4):
    print(sys.argv[0], ": takes 3 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: width height.")
    print("Example:", sys.argv[0], " 200 300 out.png")
    sys.exit()
cols = int(sys.argv[1])
rows = int(sys.argv[2])
name_output = sys.argv[3]

# compute the output image
image = np.zeros([rows, cols, 3], dtype='uint8') # Initialize the image with all 0
for i in range(0, rows):
    for j in range (0,cols):
        # 0≤L≤100 , −134≤u≤220, −140≤v≤122
        L = 90
        u = (354 * j / cols) - 134
        v = (262 * i / rows) - 140
        b,g,r = convertColors.convertLuv2BGR(L,u,v)
        image[i,j]=np.array([b,g,r],dtype='uint8')

# display and write the output image
cv2.imshow("Luv", image)
cv2.imwrite(name_output, image)

# wait for key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
