import cv2
def calculate_humans(path):
   img = cv2.imread(path)
   img = cv2.resize(img, (700,400))

   # initialize the HOG descriptor
   hog = cv2.HOGDescriptor()
   hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

   # detect humans in input image
   (humans, _) = hog.detectMultiScale(img, winStride=(4, 4),
   padding=(4, 4), scale=1.1)
   return len(humans)

