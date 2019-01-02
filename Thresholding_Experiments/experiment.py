import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wd




img = cv.imread("../xview_dataset/train_images/8.tif",0)

if img is None:
    print("Did not load image")
    exit(1)

fig, ax = plt.subplots()
thresh = 127
axcolor = 'lightgoldenrodyellow'
def run_thresh(thresh):
    ret,thresh1 = cv.threshold(img,thresh,255,cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(img,thresh,255,cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(img,thresh,255,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,thresh,255,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,thresh,255,cv.THRESH_TOZERO_INV)
    return thresh1, thresh2, thresh3, thresh4, thresh5

axthresh = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slthresh = wd.Slider(axthresh, 'Threshold', 1, 255, valinit=127)

def update():
    run_thresh(slthresh.val)
    fig.canvas.draw_idle()

slthresh.on_changed(update)

images = [img]
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']

for result in run_thresh(thresh):
    images.append(result)


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()