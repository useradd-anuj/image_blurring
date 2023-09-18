import cv2
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)


while True:
    ret, photo = cap.read()
    gray = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    try:
        faces = (face_classifier.detectMultiScale(gray, 1.3, 5)[0])
    except:
        pass

    if len(faces)!=0:
        try:
            x,y,w,h=faces
            print(x,y,w,h)
            print(faces)
            photo[y:y+h, x:x+w]=cv2.blur(photo[y:y+h, x:x+w],(50,50))
            print("to show")
            cv2.imshow("window",photo)
        except:
            pass
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()

cap.release()
