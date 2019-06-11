# Finger_Detection
Python program detect how many fingers are shown through the webcam using OpenCV and with the application of Convex Hull 

Summary

Process:

- After getting the frame as image source through the webcam, we convert the frame into HSV color. 
- Using trackbars of value lowH, lowS, lowV, highS, highH and high V to remove the back ground and get the hand 
- We then draw the contours of the hand by using the Convex Hull algorithm and use the area factor (area condition > some number)
  to remove the noise from the background, extract only the hand 
- To extract the hand more precise, we then use the convexityDefects to get the defects points
- From the defect points, we can determine how many fingers are shown 

Notes:

- There is no track bar on the program because after using the track bars to determine 6 values, I already got 1 constant value that 
was appropriate for extracting the hand only, which is: lowH: 0, lowS: 58, lowV: 140, highH: 57, highS: 255, highV: 255
- With the defect points, we have to set some conditions for those points. The convexityDefects function will return 3 points:
    + the starting point of the defect
    + the ending point of the defect
    + the farthest point fromm the defects line
  Our fingers often create an angle < 90 degrees, which contribute 1 condition for the extraction. To get the angle, we calculate the
  length of each line and then use the law of cosines to determine the angle degree. Furthermore, we have to determine the appropriate 
  length of lines from starting point to the farthest point. We also need to consider the y coordinate
  of the starting point must lay above the y coordinate of the farthest point. 

Flaws:

- The program has not had the perfect condition to extract the fingers only
- The program could not detect any finger in the case there is only 1 finger was shown. That was because the angle of fingers has
to be created from 2 fingers

References: 
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html
https://picoledelimao.github.io/blog/2015/11/15/fingertip-detection-on-opencv/
