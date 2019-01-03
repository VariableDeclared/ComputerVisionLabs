import cv2 as cv


edgeThresh = 3
lowThreshold = 100
max_lowThreshold = 255
ratio = 3
kernel_size = 3
window_name = "Window Name"


img = cv.imread('../xview_dataset/train_images/5.tif')

if img is None:
    print("Could not open file")
    exit(0)

img = cv.blur(img, (4, 4))

img = cv.Canny(img, lowThreshold, lowThreshold*ratio)

cv.namedWindow(window_name)

cv.imshow(window_name, img)


cv.waitKey(0)