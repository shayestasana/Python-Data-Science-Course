
# to close by esc button
import cv2
from datetime import datetime

def get_time():
    return datetime.now().strftime("%H:%M:%S")

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, image = webcam.read()
    if not status:
        print("Camera not working")
        break

    h,w,_=image.shape
    image=cv2.resize(image, (w*2, h*2))

    msg="Camera 0: Live Feed"
    pos=(10, 30)
    font= cv2.FONT_HERSHEY_COMPLEX
    color=(0, 255, 0)  # BGR --> 0,Green,0    
    cv2.putText(image, msg, pos, font, 1, color, 2)
    cv2.putText(image, get_time(), (10,60), font, .5, color, 2)

    cv2.imshow("Webcam", image)
    # press esc to exit 
    if cv2.waitKey(5) == 27:
        break
webcam.release()
cv2.destroyAllWindows()