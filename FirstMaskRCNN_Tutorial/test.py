import cv2 as cv



cv.namedWindow("Feed", cv.WINDOW_AUTOSIZE)

vs = cv.VideoCapture(0)
while True:
    (grabbed, frame) = vs.read()


    cv.imshow("Feed", frame)

    cv.waitKey(0)