__author__ = 'jssmith'

import cv2
from epics import PV

camera = cv2.VideoCapture(0)
# camera2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

ts = PV('S:IOC:timeOfDayForm1SI')
# tk = PV('IDBPTC10:Channel:user2_VAL')

out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
out2 = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

while camera.isOpened():

    ret, frame = camera.read()

    if ret:
        # frame = cv2.flip(frame,0)
        # cv2.putText(frame, alpha, (50, 460), cv2.FONT_ITALIC, 0.8, (255, 255, 255))
        cv2.putText(frame, ts.value, (50, 400),  5, 0.8, (255, 255, 255))
        # cv2.putText(frame2, ts.value, (50, 400), 5, 0.8, (255, 255, 255))
        # cv2.putText(frame, hotness, (50, 430), 5, 0.8, (255, 255, 255))

        # write the flipped frame
        out.write(frame)

        cv2.imshow('LiveFeed-LOM', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished

camera.release()
out.release()
cv2.destroyAllWindows()
