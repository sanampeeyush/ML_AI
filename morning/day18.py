import cv2
from time import sleep
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
vid = cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bounding_boxes, weigths = hog.detectMultiScale(img_gray, winStride=(10,10))
        for x,y,w,h in bounding_boxes:
            cv2.rectangle(
                img, pt1=(x,y), pt2=(x+w, y+h),
                color=(0,0,255), thickness=8,
            )
        sleep(0.1)
        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
cv2.destroyAllWindows()
cv2.waitKey(1) # MacOS
vid.release()