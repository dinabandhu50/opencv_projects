import cv2

# capture video
cap = cv2.VideoCapture(0)

if(cap.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create videowriter object
out = cv2.VideoWriter(
    '../data/outpy.avi',
    cv2.VideoWriter_fourcc('M', "J", "P", "G"),
    10,
    (frame_width, frame_height)
)

while(True):
    ret, frame = cap.read()

    if ret == True:
        # writing the frame into the outpy file
        out.write(frame)
        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Press Q on to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# when every thing done release all
out.release()
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
