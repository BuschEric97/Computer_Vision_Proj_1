# CS4391.001 - Project 1
#
# This file contains the functions
# to convert between color spaces
#
# Program by: Eric Busch
# edb160230@utdallas.edu

import cv2
import numpy as np
import math

def convertLuv2XYZ(L,u,v):
    # compute u' and v' from uw and vw; if division by zero, set to zero
    uw = (4 * 0.95) / (0.95 + 15 + (3 * 1.09))
    vw = 9 / (0.95 + 15 + (3 * 1.09))
    if (L == 0):
        up = 0
        vp = 0
    else:
        up = (u + (13 * uw * L)) / (13 * L)
        vp = (v + (13 * vw * L)) / (13 * L)

    # compute Y
    if (L > 7.9996):
        Y = math.pow(((L + 16) / 116), 3)
    else:
        Y = L / 903.3

    # compute X and Z; if division by zero, set to zero
    if (L == 0):
        X = 0
        Z = 0
    else:
        X = Y * 2.25 * (up / vp)
        Z = (Y * (3 - (0.75 * up) - (5 * vp))) / vp

    return X,Y,Z

def convertXYZ2linRGB(X,Y,Z):
    # compute R, G, and B
    R = (3.240479 * X) + (-1.53715 * Y) + (-0.498535 * Z)
    G = (-0.969256 * X) + (1.875991 * Y) + (0.041556 * Z)
    B = (0.055648 * X) + (-0.204043 * Y) + (1.057311 * Z)

    # clip value of R, G, and B if needed
    if (R < 0):
        R = 0
    if (R > 1):
        R = 1
    if (G < 0):
        G = 0
    if (G > 1):
        G = 1
    if (B < 0):
        B = 0
    if (B > 1):
        B = 1

    return R,G,B

def gammaCorrect(u):
    if (u < 0.00304):
        return 12.92 * u
    else:
        return (1.055 * math.pow(u, 1 / 2.4)) - 0.055

def invGammaCorrect(v):
    if (v < 0.03928):
        return v / 12.92
    else:
        return math.pow(((v + 0.055) / 1.055), 2.4)

def convertlinRGB2sRGB(lR,lG,lB):
    # compute non-linear R,G,B
    nlR = gammaCorrect(lR)
    nlG = gammaCorrect(lG)
    nlB = gammaCorrect(lB)

    # multiply by 255 and round to nearest integer
    R = math.floor((nlR * 255) + 0.5)
    G = math.floor((nlG * 255) + 0.5)
    B = math.floor((nlB * 255) + 0.5)

    return R,G,B

def convertLuv2BGR(L,u,v):
    # go through the steps of converting Luv to BGR
    X,Y,Z = convertLuv2XYZ(L,u,v)
    lR,lG,lB = convertXYZ2linRGB(X,Y,Z)
    R,G,B = convertlinRGB2sRGB(lR,lG,lB)

    return B,G,R

def convertsRGB2linRGB(sR,sG,sB):
    # divide by 255
    R = sR / 255.0
    G = sG / 255.0
    B = sB / 255.0

    # compute linear R,G,B
    lR = invGammaCorrect(R)
    lG = invGammaCorrect(G)
    lB = invGammaCorrect(B)

    return lR,lG,lB

def convertlinRGB2XYZ(R,G,B):
    # compute X, Y, and Z
    X = (0.412453 * R) + (0.35758 * G) + (0.180423 * B)
    Y = (0.212671 * R) + (0.71516 * G) + (0.072169 * B)
    Z = (0.019334 * R) + (0.119193 * G) + (0.950227 * B)

    # clip value of X, Y, and Z if needed
    if (X < 0):
        X = 0
    if (X > 1):
        X = 1
    if (Y < 0):
        Y = 0
    if (Y > 1):
        Y = 1
    if (Z < 0):
        Z = 0
    if (Z > 1):
        Z = 1

    return X,Y,Z

def convertXYZ2Luv(X,Y,Z):
    # compute uw, vw, up, and vp; if division by zero, set to zero
    uw = (4 * 0.95) / (0.95 + 15 + (3 * 1.09))
    vw = 9 / (0.95 + 15 + (3 * 1.09))
    if (X == 0 and Y == 0 and Z == 0):
        up = 0
        vp = 0
    else:
        up = (4 * X) / (X + (15 * Y) + (3 * Z))
        vp = (9 * Y) / (X + (15 * Y) + (3 * Z))

    # compute L. Y = t for our purposes
    if (Y > 0.008856):
        L = (116 * math.pow(Y, 1/3)) - 16
    else:
        L = 903.3 * Y

    # compute u and v
    u = 13 * L * (up - uw)
    v = 13 * L * (vp - vw)

    return L,u,v

def convertBGR2Luv(B,G,R):
    # go through the steps of converting BGR to Luv
    lR,lG,lB = convertsRGB2linRGB(R,G,B)
    X,Y,Z = convertlinRGB2XYZ(lR,lG,lB)
    L,u,v = convertXYZ2Luv(X,Y,Z)

    return L,u,v
