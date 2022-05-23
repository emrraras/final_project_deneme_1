
# from bs4 import BeautifulSoup
# import requests
import pytesseract
import cv2

# url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
# r=requests.get(url1,verify=False) #
# soup = BeautifulSoup(r.content,'html.parser')
# gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
# ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
# ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
# onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
# onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)
# print(onikimetrekupalti,onikimetrekupustu) 

# import smtplib                                                    #Kütüphanemizi çağırıyoru
# content = "kayıtedildi"                                               #content adında mesajımızı oluşturuyoruz
# mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
# mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
# mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
# mail.login("mertcan.igdir@gmail.com","2000mmmm")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
# mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz


# import time
# import datetime

# t="%d:%m:%Y"
# s="%H:%M:%S"
# # gün="%d"
# # ay="%m"
# # yıl="%Y"
# # saat="%H"
# dakika="%M"
# saniye="%S"

# tarih=time.strftime(t)
# saatg=time.strftime(s)
# Gün=int(time.strftime(saniye))
# print(tarih,saatg)
# print(Gün)
# istenilenzaman=datetime.datetime(20,44,21)

# gecti=int(time.strftime(saniye))+1
# print(gecti)
# while 1:
#     if gecti == Gün:
#         print("oldu")
#         print(saatg)
#         break
#######################################################################
# import cv2
# import os
# import time
# def oku():
#     import pytesseract
#     # pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\emrea\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'    # tesseract.exe nin bilgisayarda kurulu olduğu yer
#     def ocr_core(img):
#         text = pytesseract.image_to_string(img)
#         return text

#     img =cv2.imread('D:\\Visual Studio\\final_project_deneme_1\\opencv_frame_0')  # okunacak resimin konumu

#     def get_grayscale(image):
#         return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#     def remove_noise(image):
#         return cv2.medianBlur(image,5)

#     def thresholding(image):
#         return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     img = get_grayscale(img)
#     img= thresholding(img)
#     img=remove_noise(img)

#     print(ocr_core(img))
#     print(type(ocr_core(img)))




# def mail_gönder():
#     import smtplib                                                    #Kütüphanemizi çağırıyoru
#     content = "fotokayıtedildi"                                               #content adında mesajımızı oluşturuyoruz
#     mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
#     mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
#     mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
#     mail.login("mertcan.igdir@gmail.com","mxcan80ertxn,")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
#     mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz
# import cv2
# from cv2 import cvtColor
# import os
# import pytesseract
# from PIL import Image
# import time


# img_counter = 0
# cam = cv2.VideoCapture(1)
# cv2.namedWindow("test")
# img_name = "opencv_frame_{}.png".format(img_counter)

# def kayit():
#     global img_counter       
    
#     cv2.imwrite(img_name, frame)
#     print("{} written!".format(img_name))
#     img_counter += 1

# def sil():
#     global img_name
#     os.remove("{}".format(img_name)) #silinecek dosyanın ismi



# def oku():
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  
# def ocr_core(img):
#     text = pytesseract.image_to_string(img)
#     return text
        

# img =cv2.imread('C:\\Users\\emrea\\Desktop\\Coding\\final_project_deneme_1\\aa.png')  # okunacak resimin konumu

# def get_grayscale(image):
#     return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# def remove_noise(image):
#     return cv2.medianBlur(image,5)

# def thresholding(image):
#     return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# img = get_grayscale(img)
# img= thresholding(img)
# img=remove_noise(img)

# print(ocr_core(img))
# print(type(ocr_core(img)))


# while True:
#     ret, frame = cam.read()
#     # cv2.imshow("test", frame)
#     time.sleep(5)
#     kayit()
#     time.sleep(3)
#     oku()
#     time.sleep(3)
#     sil()

# ###################################################3

# from gettext import gettext
# from html.parser import HTMLParser
# from tkinter import Frame
# import cv2
# import pytesseract
# from PIL import Image
# from lib2to3.pgen2 import driver
# from selenium import webdriver                                             # burdaki import ile chrome üzerinden herhangi bir sayfaya giriş yapmamızı sağlıyor
# import time 
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from bs4 import BeautifulSoup
# import numpy as np
# import pytesseract

# ( sideden veri çekme uygulaması)

# url1="https://www.buski.gov.tr/AboneRehberi/AboneRehberi/7" #çalışacağmız site
# r=requests.get(url1,verify=False) 
# soup = BeautifulSoup(r.content,'html.parser')
# gelen_veri= soup.find_all("table",{"class":"table table-bordered table-striped"}) #almak istediğimiz verinin içinde bulunduğu geniş alan 
# ucret= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
# ucret=ucret.find_all('td',style="text-align:center") #almak istediğimiz verinin içinde bulunduğu satır
# onikimetrekupustu = ucret[1].text #almak istediğimiz veri  (text halinde)
# onikimetrekupalti = ucret[0].text #almak istediğimiz veri  (text halinde)
# print(onikimetrekupalti,onikimetrekupustu) 


#################################################################### mail gönderme



# def mail_gönder():
#     import smtplib                                                    #Kütüphanemizi çağırıyoru
#     content = "fotokayıtedildi"                                               #content adında mesajımızı oluşturuyoruz
#     mail = smtplib.SMTP("smtp.gmail.com",587)                         #SMTP'nin gmail aderine 587. porttan ulaşıyoruz#
#     mail.ehlo()                                                       #ehlo fonksiyonu ile kullanılabilir hale getiriyoruz
#     mail.starttls()                                                   #starttls fonksiyonu ile bağlantımızı gizli hale getiriyoruz
#     mail.login("mertcan.igdir@gmail.com","mxcan80ertxn,")                            #login fonksiyonu ile herhangi bir mail adresine giriş yapıyoruz
#     mail.sendmail("mertcan.igdir@gmail.com","igdir.mertcan@gmail.com",content.encode("utf-8"))      #sendmail fonksiyonu ile göndereni, alıcıyı ve gönderilen metni belirliyoruz
#     print("Gönderildi")


################## kamera açma ve kaydetme

    ################################# dosya silme baslangıç
# def sil():
#     import os
#     os.remove("{}".format(img_name)) #silinecek dosyanın ismi
            
#     ################################# dosya silme bitiş
# def kayıt():
#     cv2.imwrite(img_name, frame)
#     print("{} written!".format(img_name)) #kaydedilecek dosyanın ismi
    


# import cv2
# import os
# img_counter = 0

# cam = cv2.VideoCapture(1) #kamera seçimi

# cv2.namedWindow("test")
# img_name = "opencv_frame_{}.png".format(img_counter)
    

# while True:
#     ret, frame = cam.read()
#     cv2.imshow("test", frame)
#     if not ret:
#         print("failed to grab frame")
#         break

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # kamerayı kapatmak için ESC ye 
#         print("Escape hit, closing...")
#         break
#     time.sleep(5)
#     kayıt()
#     time.sleep(5)
#     # oku()
#     # time.sleep(5)
#     sil()

# cam.release()

# cv2.destroyAllWindows(0)
        
# import cv2
# from PIL import Image
# im1 =Image.open('C:\\Users\\emrea\\Desktop\\Coding\\final_project_deneme_1\\aa.jpg')
# im1.save('C:\\Users\\emrea\\Desktop\\Coding\\final_project_deneme_1\\aa.png')

# def oku():
#     import cv2
#     import pytesseract
#     def ocr_core(img):
#         text = pytesseract.image_to_string(img)
#         return text
        

#     img =cv2.imread('C:\\Users\\emrea\\Desktop\\Coding\\final_project_deneme_1\\aa.png')  # okunacak resimin konumu

#     def get_grayscale(image):
#         return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#     def remove_noise(image):
#         return cv2.medianBlur(image,5)

#     def thresholding(image):
#         return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     img = get_grayscale(img)
#     img= thresholding(img)
#     img=remove_noise(img)

#     print(ocr_core(img))
#     print(type(ocr_core(img)))
# oku()
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\emrea\\Desktop\\Coding\\yeni_d-zen\\New folder\\tesseract.exe'

a=pytesseract.image_to_string(Image.open('abc.png'), lang="eng")

print(a)