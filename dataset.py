import time
import cv2 as cv
import os

camera = cv.VideoCapture(1)
# camera.set(cv.CAP_PROP_AUTOFOCUS, 0)

if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()

Labels = ["negatif"]
for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)

for folder in Labels:
    count = 0
    print("Press 'p' to start data collection for "+ folder)
    userinput = input()
    if userinput != 'p':
        print("Exit System..........")
        exit()
    
    while count<700:
        status, frame = camera.read()
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        f1 = cv.resize(frame, (1344,761))
        cv.imshow("Dataset Maker",f1)
        frame = cv.resize(frame, (1344,761))
        cv.imwrite('C:\\Users\\ASUS\\Road-Surface-Classification\\input-dataset-compressed-2\\negatif'+folder+'\\'+str(folder)+' ('+str(count)+').jpg',frame)
        count=count+1
      
        if cv.waitKey(1) == ord('q'):
            break
        elif cv.waitKey(1) == ord('s'):
            print ('Selesai')
            time.sleep(2)

camera.release()
cv.destroyAllWindows()