import cv2
import infer

cap_i = cv2.VideoCapture(0)



while True:
    ref, frame = cap_i.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

    infer.main('--source frame')

