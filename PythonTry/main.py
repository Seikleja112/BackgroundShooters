import cv2
import numpy as np

def most_common(lst):
    return max(set(lst), key=lst.count)

img0 = cv2.imread('D:/Desktop/Digital Image processing/BackgroundShooters/SampleImages/Selfmade/0.jpg', 0)
img1 = cv2.imread('D:/Desktop/Digital Image processing/BackgroundShooters/SampleImages/Selfmade/1.jpg', 0)
img2 = cv2.imread('D:/Desktop/Digital Image processing/BackgroundShooters/SampleImages/Selfmade/2.jpg', 0)
img3 = cv2.imread('D:/Desktop/Digital Image processing/BackgroundShooters/SampleImages/Selfmade/3.jpg', 0)
img4 = cv2.imread('D:/Desktop/Digital Image processing/BackgroundShooters/SampleImages/Selfmade/clear.jpg', 0)

#cv2.imshow("original",img0)




cv2.waitKey(0)

height, width = img0.shape
print(img0.shape)
new = np.zeros((height, width))
new = np.uint64(new)

new1 = np.zeros((height, width))
new1 = np.uint64(new)

new2 = np.zeros((height, width))
new2 = np.uint64(new)


for i in range(height):
    for j in range(width):
        x=[]
        x.append(img0[i,j])
        x.append(img1[i, j])
        x.append(img2[i, j])
        x.append(img3[i, j])
        #x.append(img4[i, j])
        x.sort()

        new[i,j] = most_common(x)
        new1[i, j] = np.median(x)
        new2[i,j] = (np.sum(x)/4)

new = np.uint8(new)
new1 = np.uint8(new1)
new2 = np.uint8(new2)

cv2.imshow("most common", new)
cv2.imshow("median", new1)
cv2.imshow("Output", new2)
cv2.waitKey(0)
#for i in range()