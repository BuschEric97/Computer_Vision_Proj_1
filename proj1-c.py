# CS4391.001 - Project 1
#
# This file is the program
# for part 2 of project 1
#
# Program by: Eric Busch
# edb160230@utdallas.edu

import cv2
import numpy as np
import sys
import modifyImage

# get and assign command line arguments
if (len(sys.argv) != 7):
    print(sys.argv[0], ": takes 6 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: w1 h1 w2 h2 ImageIn ImageOut.")
    print("Example:", sys.argv[0], " 0.2 0.1 0.8 0.5 fruits.jpg out.png")
    sys.exit()
w1 = float(sys.argv[1])
h1 = float(sys.argv[2])
w2 = float(sys.argv[3])
h2 = float(sys.argv[4])
name_input = sys.argv[5]
name_output = sys.argv[6]

# check that command line arguments 1-4 are valid
if(w1<0 or h1<0 or w2<=w1 or h2<=h1 or w2>1 or h2>1) :
    print(" arguments must satisfy 0 <= w1 < w2 <= 1, 0 <= h1 < h2 <= 1")
    sys.exit()

# read and display input image
inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)
if(inputImage is None) :
    print(sys.argv[0], ": Failed to read image from: ", name_input)
    sys.exit()
cv2.imshow("Original Image", inputImage)

# compute W1, H1, W2, H2 which are the values for
# the range of the image in which we are modifying
rows, cols, bands = inputImage.shape # bands == 3
W1 = round(w1*(cols-1))
H1 = round(h1*(rows-1))
W2 = round(w2*(cols-1))
H2 = round(h2*(rows-1))

# transform the image on the range previously computed
outputImage = modifyImage.histogramEqual(W1, H1, W2, H2, inputImage)

# display and write output image
cv2.imshow("Modified Image", outputImage)
cv2.imwrite(name_output, outputImage);

# wait for key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
