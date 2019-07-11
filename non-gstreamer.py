import numpy as np
import os
import cv2

def main():
    # cap = cv2.VideoCapture('./videos/18.avi')
    cap = cv2.VideoCapture('rtsp://admin:vDspa$$w0rd@113.22.74.74:1555')
    ROI = [0.05, 0.1, 0.5, 0.5]  # htop, wleft, hbot, wright
    ROI = [0, 0, 1, 1]
    while cap.isOpened():
        # Grab a single frame of video
        ret, frame = cap.read()
        
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
