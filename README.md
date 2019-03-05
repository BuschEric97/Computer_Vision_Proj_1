# Computer_Vision_Proj_1

You are asked to write four programs, all related to the manipulation of color in digital images.

First program
Write a program that displays continuous changes in color for Luv representation. The input to the program
is a width and a height. The output is an image of dimension width × height that is displayed on the screen.
For the image created, the pixel at row i and column j should have the color value:
L = 90, u = 354 ∗ j/width − 134, v = 262 ∗ i/height − 140
The main programming effort is writing the routine to convert Luv pixels to RGB. The provided example
program proj1a.py does everything with the exception of this conversion. It is recommended that you write
your program by changing proj1a.py so that it fulfills the requirements.

Second, third and fourth program

These programs change the color of a specified window of the image based on a histogram computed from
that window in the image. The window is specified in terms of the normalized coordinates w1, h1, w2, h2,
where the window upper left point is (w1, h1), and its lower right point is (w2, h2). For example, w1 = 0,
h1 = 0, w2 = 1, h2 = 1 is the entire image, and w1 = 0.3, h1 = 0.3, w2 = 0.7, h2 = 0.7 is window in the
center of the image. The provided example program proj1b.py shows how to go over the pixels of this
window.

Second program

Write a program that gets as input a color image, performs linear scaling in the Luv domain, and writes the
scaled image as output.
Pixel values outside the window should not be changed. Only pixels within the window should be changed
with scaled values.
The scaling in Luv should stretch only the luminance values. You are asked to apply linear scaling that
would map the smallest L value in the specified window to 0, and the largest L value in the specified
window to 100.

Third program

Write a program that gets as input a color image, performs histogram equalization in the Luv domain, and
writes the scaled image as output. Histogram equalization in Luv is applied to the luminance values, as
computed in the specified window. It requires a discretization step, where the real-valued L is discretized
into 101 values.
As in the second program pixel values outside the window should not be changed. Only pixels within
the window should be changed.

Fourth program

This is the same as the third program, except openCV functions for color coversion and histogram equalization should be used for the pixels in the specified window.
