import cv2
import pyzbar.pyzbar as pyzbar
from gtts import gTTS
import numpy as np

used_codes = []

try:
    f = open("qrbarcode_data.txt","r",encoding="utf8")
    data_list = f.readlines()
except FileNotFoundError:
    pass
else:
    f.close()

    for i in data_list:
        used_codes.append(i.rstrip('\n'))


        #Set file name here

        inputImage = cv2.imread("qrcodesample.jpg")   
        inputImage = cv2.resize(inputImage, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

        qrDecoder = cv2.QRCodeDetector()


        data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
    
        if len(data)>0:
            print("Decoded Data : {}".format(data))

            rectifiedImage = np.uint8(rectifiedImage)
            f2 = open("qrbarcode_data.txt", "a", encoding="utf8")
            f2.write(format(data)+'\n')
            f2.close()
    
        else:
            print("QR Code not detected")


    textpath = 'qrbarcode_data.txt'

with open(textpath, mode='r', encoding='UTF-8') as text:
        script = text.read()

script.replace('\n', '') 
speech = gTTS(text=script, lang='en') 
speech.save('sample.mp3')



