import cv2
from time import sleep

fd = cv2.CascadeClassifier(
    cv2.data.haarcascades + 
    'haarcascade_frontalface_default.xml'
)
vid = cv2.VideoCapture(0)

while True:
    flag, img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        x1, y1, w, h = (200, 400, 300, 400)

        faces = fd.detectMultiScale(img_gray, 1.1, 5)

        for x1,y1,w,h in faces:

            img_cropped = img[y1:y1+h, x1:x1+w, :]

            cv2.rectangle(
                img, 
                pt1=(x1,y1), pt2=(x1+w, y1+h),
                color=(0,0,255), thickness=10
            )

        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)
        if key == ord('x'):
            break
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()

cv2.waitKey(10)  # Only for Mac OS,  not for Windows