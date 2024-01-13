import cv2

img = cv2.imread('zdjecie.png')
img = cv2.resize(img, (700,400))

# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# detect humans in input image
(humans, _) = hog.detectMultiScale(img, winStride=(2, 2),
padding=(32, 32), scale=1.1)

# getting no. of human detected
print('Human Detected : ', len(humans))

# loop over all detected humans
for (x, y, w, h) in humans:
   pad_w, pad_h = int(0.15 * w), int(0.01 * h)
   cv2.rectangle(img, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

# display the output image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
