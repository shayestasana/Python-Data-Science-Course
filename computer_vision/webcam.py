
# to close by esc button
import cv2

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, frame = webcam.read()
    if not status:
        print("Camera not working")
        break
    cv2.imshow("Webcam", frame)
    # press esc to exit 
    if cv2.waitKey(5) == 27:
        break
webcam.release()
cv2.destroyAllWindows()