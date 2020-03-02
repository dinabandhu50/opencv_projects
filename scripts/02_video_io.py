import cv2


# Reading video
cap = cv2.VideoCapture('../data/seniorita.mp4')

#  loop
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Video finished")
        break

cap.release()
cv2.destroyAllWindows()
