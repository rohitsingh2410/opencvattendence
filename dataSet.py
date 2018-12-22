def data():
    
    import numpy as np
    import cv2

    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0);

    id=input("enter user id: ")
    samplenumber=0;
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5);
        for (x,y,w,h) in faces:
            samplenumber=samplenumber+1;
            cv2.imwrite("dataset/user."+str(id)+"."+str(samplenumber)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.waitKey(100);

        cv2.imshow('face',img)
        cv2.waitKey(1);
        if(samplenumber>50):
            break
    cam.release()
    cv2.destroyAllWindows()

