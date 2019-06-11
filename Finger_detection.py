import cv2 as cv
import numpy as np
import math

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (0, 58, 140), (57, 255, 255))

    ret, thresh = cv.threshold(frame_threshold, 50, 255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    hull = []
    for i in range(len(contours)):
        hull.append(cv.convexHull(contours[i], False))
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    for i in range(len(contours)):
        color_contours = (0, 255, 0)
        color = (255, 0, 0)
        area = cv.contourArea(contours[i])
        if area > 3000:
            contours[0] = contours[i]
            cv.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
            cv.drawContours(drawing, hull, i, color, 1, 8)

    cnt = contours[0]

    hulll = cv.convexHull(cnt, returnPoints=False)
    defects = cv.convexityDefects(cnt, hulll)
    temp = 0
    if (not (defects is None)):
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            l1 = ((start[0] - far[0]) * (start[0] - far[0]) + (start[1] - far[1]) * (start[1] - far[1])) ** 0.5
            l2 = ((end[0] - far[0]) * (end[0] - far[0]) + (end[1] - far[1]) * (end[1] - far[1])) ** 0.5
            l3 = ((start[0] - end[0]) * (start[0] - end[0]) + (start[1] - end[1]) * (start[1] - end[1])) ** 0.5
            rad = math.acos((l1 ** 2 + l2 ** 2 - l3 ** 2) / (2 * l1 * l2))

            if ((math.degrees(rad) < 90) and (l1 > 40) and (start[1] < far[1])):
                temp = temp + 1
                line1 = cv.line(drawing, start, far, [0, 0, 255], 2)
                line2 = cv.line(drawing, far, end, [0, 0, 255], 2)
                cv.circle(drawing, far, 5, [0, 0, 255], -1)

    cv.imshow("Thresh_hold", frame_threshold)
    cv.imshow("Finger Detection with COnvexHull", drawing)
    print(temp + 1)

    key = cv.waitKey(30)
    if key == ord('q'):
        break
