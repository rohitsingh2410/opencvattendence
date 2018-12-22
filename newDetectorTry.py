

def csvprint(name):
    print(name)
    text_file = open("attendence.txt", "a+")
    if str(name) in open('attendence.txt').read():
        pass
    else:
        
        from datetime import datetime
        date=datetime.now().strftime('%Y-%m-%d ')
        time=datetime.now().strftime(' %H:%M:%S')
        #myData = [[1, 2, 3], [str(id), str(date), str(time)]]  
        
        text_file.write(name +  date +  time)
        text_file.close()
    
def detect():
    import cv2
    import numpy as np

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);


    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            print('face matched',Id)
            if(conf<50):
                if(Id==1):
                    Id="Rohit"
                    csvprint(Id)
                    
                elif(Id==2):
                    Id="john lees"
                    csvprint(Id)
                elif(Id==3):
                    Id="akash"
                    csvprint(Id)
                elif(Id==5):
                    Id="Chairman Sir"
                    csvprint(Id)
            
            else:
                Id="Unknown"
            #cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
            cv2.putText(im, str(Id), (x,y-40),font, 1, (255,255,255), 3)
        cv2.imshow('im',im) 
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
