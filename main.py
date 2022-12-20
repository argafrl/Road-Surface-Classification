
import cv2
import numpy as np
from PIL import Image
from keras import models
import time
import serial
import tensorflow as tf

ArduinoSerial=serial.Serial('com7',9600,timeout=0.1)

time.sleep(1)

model = models.load_model('modelMobileNetV2-181222.h5')

video = cv2.VideoCapture("./Pengujian/Pengujian_Kerikil_Compressed.mp4")
# video = cv2.VideoCapture(1)
# video.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off

isStop = 0
threshold = 0.93
count = 0
string = ""

while True:
        _, frame = video.read()
        gray = frame
        startTime = time.time()
        # frame_copy = frame[52:180,96:224] # Video 320 (L) X 180 (T)
        # frame_copy = frame[300:480,230:410] # Webcam Laptop
        # frame_copy = frame[680:1080,760:1160] # Video 1920 X 1080
        if (frame.shape[0] <= 480 and frame.shape[1] <= 640):
                frame_copy = frame[300:480,230:410]
        elif (frame.shape[0] <= 768 and frame.shape[1] <= 1366):
                frame_copy = frame[461:761,522:822]
        elif (frame.shape[0] <= 1080 and frame.shape[1] <= 1920):
                frame_copy = frame[680:1080,760:1160]
        
        im = Image.fromarray(frame_copy, 'RGB')
        im = im.resize((128,128))

        img_array = np.array(im)
        img_array_expand = np.expand_dims(img_array, axis=0)

        input_arr = np.array([img_array])
        input_arr = input_arr.astype('float32') / 255.
        pred = model.predict(input_arr)
        predicted_class = np.argmax(pred, axis=-1)

        accuration = np.max(pred)
        count += 1
        print("Frame ke-", count)

        if(predicted_class == 0 and accuration > threshold):
                # kelas = "Aspal"
                print("Kelas: Aspal")
                print("Accuration: ", accuration)
                string = "0"
        elif(predicted_class == 1 and accuration > threshold):
                # kelas = "Kerikil"
                print("Kelas: Kerikil")
                print("Accuration: ", accuration)
                string = "1"
        elif(predicted_class == 2 and accuration > threshold):
                # kelas = "Lantai"
                print("Kelas: Lantai")
                print("Accuration: ", accuration)
                string = "2"
        elif(predicted_class == 3 and accuration > threshold):
                # kelas = "Negatif"
                print("Kelas: Negatif")
                print("Accuration: ", accuration)
                string = string
        elif(predicted_class == 4 and accuration > threshold):
                # kelas = "Paving"
                print("Kelas: Paving")
                print("Accuration: ", accuration)
                string = "4"

        pwmValue = ArduinoSerial.readline().decode().strip()
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
                isStop = 1
                string = "5"
        if(isStop == 1 and pwmValue == "0 - 0"):
                print("Program Stopped")
                break

        ArduinoSerial.write(bytes(string, 'utf-8'))
        cv2.imshow("Capturing", frame)
        cv2.imshow("Capturing ROI", frame_copy)

        endTime = time.time()
        print("PWM:", pwmValue)
        print("Waktu:", endTime-startTime)
        print("")

video.release()
cv2.destroyAllWindows()