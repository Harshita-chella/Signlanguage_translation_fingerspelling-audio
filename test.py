import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pyttsx3
import threading
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
offset = 20
imgSize = 300
engine = pyttsx3.init()
engine.setProperty('rate', 100)
labels = ["A", "B", "C",'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','HELLO','I LOVE YOU','I REALLY LOVE YOU','PLEASE','YES','OKAY','THANK YOU','HOW']

# labels = ['Hello','Okay','Thank you','Yes','Good Morning','Please','No','Bye','I Love You','Your Welcome','Sorry','Little','A','B','C','D','E','F','G','I','L','R','U']

sentence = ''
prediction_made = False
hands_detected_time = None
prediction_delay = 2.0  # seconds

def make_prediction():
    global prediction_made
    global sentence
    global hands_detected_time
    prediction_made = True
    hands_detected_time = None
    hand = hands[0]
    x, y, w, h = hand['bbox']

    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

    imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
    imgCropShape = imgCrop.shape

    aspectRatio = h / w

    if aspectRatio > 1:
        k = imgSize / h
        wCal = math.ceil(k * w)
        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
        imgResizeShape = imgResize.shape
        wGap = math.ceil((imgSize-wCal)/2)
        imgWhite[:, wGap: wCal + wGap] = imgResize
        prediction , index = classifier.getPrediction(imgWhite, draw=False)
        res = labels[index]
        if res == 'SPACE':
            sentence += ' '
        else:
            sentence += str(res)
            engine.say(res)
            engine.runAndWait()
        print(res)
    else:
        k = imgSize / w
        hCal = math.ceil(k * h)
        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
        imgResizeShape = imgResize.shape
        hGap = math.ceil((imgSize - hCal) / 2)
        imgWhite[hGap: hCal + hGap, :] = imgResize
        prediction , index = classifier.getPrediction(imgWhite, draw=False)
        res = labels[index]
        if res == 'SPACE':
            sentence += ' '
        else:
            sentence += str(res)
            engine.say(res)
            engine.runAndWait()
        print(res)

        cv2.rectangle(imgOutput, (x-offset, y-offset-70), (x-offset+400, y-offset+60-50), (0,255,0), cv2.FILLED)  
        cv2.putText(imgOutput, labels[index], (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2) 
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w + offset, y+h + offset), (0,255,0), 4)  

while True:
    try:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        
        if hands and not prediction_made:
            if hands_detected_time is None:
                hands_detected_time = time.time()
            elif time.time() - hands_detected_time >= prediction_delay:
                threading.Thread(target=make_prediction).start()
        elif not hands and prediction_made:
            prediction_made = False
        
        cv2.imshow('Image', imgOutput)
        
        # Check for space key press
        key = cv2.waitKey(1)
        if key == 32:  # 32 is ASCII code for space
            sentence += ' '
            print("Space added to sentence")

        if key == 27:  # 27 is ASCII code for 'Esc' key
            print(sentence)
            engine.runAndWait()
            engine.say(sentence)
            engine.runAndWait()
            sentence=''
            continue
        if key == ord('z'):
            break
    
    except Exception as exp:
        pass

# Speak out the sentence after exiting the loop

