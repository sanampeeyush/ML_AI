import cv2
import numpy as np
from time import sleep
fd=cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
)
sd=cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_smile.xml'
)
vid = cv2.VideoCapture(0)
notCaptured = True
while notCaptured:
    flag, img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(
            img_gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (50,50)
        )
        np.random.seed(50)
        colors = np.random.randint(0,255, (len(faces), 3)).tolist() 
        i = 0
        for x,y,w,h in faces:
            face = img_gray[y:y+h, x:x+w].copy()
            smiles = sd.detectMultiScale(
                face,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (50,50)
            )

            if len(smiles) == 1:
                cv2.imwrite('myselfie.png', img)
                notCaptured = False
                break

            cv2.rectangle(
                img, pt1=(x,y), pt2=(x+w, y+h), color=colors[i],
                thickness=8
            )
            i += 1
        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        print('No Frames')
        break
    sleep(0.1)
cv2.destroyAllWindows()
cv2.waitKey(1)
vid.release()
del vid




# import cv2
# import numpy as np
# from time import sleep
# fd=cv2.CascadeClassifier(
#     cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
# )
# sd=cv2.CascadeClassifier(
#     cv2.data.haarcascades+'haarcascade_smile.xml'
# )
# vid = cv2.VideoCapture(0)
# while True:
#     flag, img = vid.read()
#     if flag:
#         img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         smiles = sd.detectMultiScale(
#             img_gray,
#             scaleFactor = 1.1,
#             minNeighbors = 5,
#             minSize = (50,50)
#         )
#         # faces = fd.detectMultiScale(
#         #     img_gray,
#         #     scaleFactor = 1.1,
#         #     minNeighbors = 5,
#         #     minSize = (50,50)
#         # )
#         np.random.seed(50)
#         # colors = np.random.randint(0,255, (len(faces), 3)).tolist() 
#         colors = np.random.randint(0,255, (len(smiles), 3)).tolist() 
                        
#         i = 0
#         for x,y,w,h in faces:
#             cv2.rectangle(
#                 img, pt1=(x,y), pt2=(x+w, y+h), color=colors[i],
#                 thickness=8
#             )
#             i += 1
        
#         cv2.imwrite('myselfie.png', img)

#         cv2.imshow('Preview', img)
#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             break
#     else:
#         print('No Frames')
#         break
#     sleep(0.1)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
# vid.release()
# del vid
