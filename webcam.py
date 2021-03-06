import numpy as np
from time import time
import data
import cv2

cap = cv2.VideoCapture(0)
# start = time()
# Open the webcam, get the video frame by frame, and then display it
# ret, frame = cap.read()
# img = np.zeros([frame.shape[0], frame.shape[1], frame.shape[2]], dtype=np.uint8)

face_cascade = cv2.CascadeClassifier('dat/haarcascade_frontalface_default.xml')
# frame_count = 0
# fps = 0
while True:
    # img.fill(0)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    """
    remove extra computations for performance
    if fps != int(frame_count/(time()-start)):
        fps = int(frame_count / (time() - start))
    framesps = ''.join(['fps: ', str(fps)])"""

    if len(faces) != 0:
        face = faces[0]
    else:
        face = [0, 0]

    """
    Remove old commands used for visualizing the face tracking to speed up the computation
    for (x, y, w, h) in faces:
        # cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 2)
        # cv2.circle(img, (x, y), (w+h)//4, (255, 0, 150), -1)
        # cv2.putText(img, framesps, (25, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        x = x"""

    yaw = face[0]
    pitch = face[1]
    print("yaw:", yaw, ", pitch:", pitch)
    data.plot3D(yaw, pitch, .01)

    """
    more of the same...
    cv2.imshow("img", img)
    cv2.imshow('frame', gray)
    frame_count += 1"""

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
