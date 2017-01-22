import numpy as np
import cv2

cap = cv2.VideoCapture(0)

_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
_FRAME_FPS = 30
out = cv2.VideoWriter('Video_Streaming_example.avi', cv2.VideoWriter_fourcc(*'X264'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))

def _video_writer(frame):
    cv2.imshow('OpenCV_Training', frame)
    return out.write(frame)


if __name__ == '__main__':

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            _video_writer(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
out.release()
cv2.destroyAllWindows()
