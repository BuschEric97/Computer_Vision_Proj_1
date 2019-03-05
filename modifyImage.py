# CS 4391.001 - Project 1
#
# This file contains the functions for
# modifying the original image over
# a specified window using both
# linear scaling and histogram equalization
#
# Program by: Eric Busch
# edb160230@utdallas.edu

import cv2
import numpy as np
import convertColors
import math

# compute linear scaling in the range specified by W1, H1, W2, H2
def linearScale(W1, H1, W2, H2, inputImage):
    histogram = np.zeros(101, int) # define the histogram array of size 101
    outputImage = np.copy(inputImage)

    # iterate through image to fill the histogram
    for i in range(H1, H2+1):
        for j in range(W1, W2+1):
            # convert b,g,r of original image to L,u,v
            B,G,R = inputImage[i, j]
            L,u,v = convertColors.convertBGR2Luv(B,G,R)

            # add L value to histogram
            histogram[int(round(L))] += 1

    # compute a by setting it to the first non-zero index from the left of the histogram
    a = 0
    for i in range(101):
        if (histogram[i] != 0):
            a = i
            break

    # compute b by setting it to the first non-zero index from the right of the histogram
    b = 100
    for i in range(101):
        if (histogram[100-i] != 0):
            b = 100 - i
            break

    # modify original image by linear scaling on the specified window of the image
    for i in range(H1, H2+1):
        for j in range(W1, W2+1):
            # convert b,g,r of original image to L,u,v
            B,G,R = inputImage[i, j]
            L,u,v = convertColors.convertBGR2Luv(B,G,R)

            # compute new L via linear scaling formula
            L = ((L - a) * 100) / (b - a)

            # convert back to b,g,r from new L,u,v and put into output image
            B,G,R = convertColors.convertLuv2BGR(L,u,v)
            outputImage[i,j] = B,G,R

    # print histogram and calculated a and b values
    print(histogram, "\na = ", a, "\nb = ", b)
    return outputImage

# compute histogram equalization in the range specified by W1, H1, W2, H2
def histogramEqual(W1, H1, W2, H2, inputImage):
    histogram = np.zeros(101, int) # define the histogram array of size 101
    accumHist = np.zeros(101, int) # define the accumulated histogram array of size 101
    outputImage = np.copy(inputImage)

    # iterate through image to fill the histogram
    for i in range(H1, H2+1):
        for j in range(W1, W2+1):
            # convert b,g,r of original image to L,u,v
            B,G,R = inputImage[i, j]
            L,u,v = convertColors.convertBGR2Luv(B,G,R)

            # add L value to histogram
            histogram[int(round(L))] += 1

    # iterate through histogram to fill the accumulated histogram
    accumHist[0] = histogram[0]
    for i in range(1, 101):
        accumHist[i] = accumHist[i-1] + histogram[i]
    numPxls = accumHist[100] # total number of pixels in image window

    # modify original image by linear scaling on the specified window of the image
    for i in range(H1, H2+1):
        for j in range(W1, W2+1):
            # convert b,g,r of original image to L,u,v
            B,G,R = inputImage[i, j]
            L,u,v = convertColors.convertBGR2Luv(B,G,R)
            L = int(round(L)) # round L to the nearest int for later calculation

            # compute new L via histogram equalization formula
            if (L == 0):
                L = math.floor((101 * accumHist[L]) / (2 * numPxls))
            else:
                L = math.floor((101 * (accumHist[L-1] + accumHist[L])) / (2 * numPxls))

            # clip L value if it is larger than 100
            if (L > 100):
                L = 100

            # convert back to b,g,r from new L,u,v and put into output image
            B,G,R = convertColors.convertLuv2BGR(L,u,v)
            outputImage[i,j] = B,G,R

    # print histogram and calculated a and b values
    print("Histogram:\n", histogram, "\nAccumulated Histogram:\n", accumHist)
    print("numPxls = ", numPxls)
    return outputImage
