import qrcode
import cv2

#import Image

img=qrcode.make("https://github.com/shouhardik")
img.save("code.jpg")
img=qrcode.make("Hello I am Shouhardik Saha")
img.save("info.jpg")

k=cv2.QRCodeDetector()
values,point,straight_qrcode=k.detectAndDecode(cv2.imread("code.jpg"))
print(straight_qrcode)# binarized qrcode

x=cv2.QRCodeDetector()
val,point,straight_qrcode=x.detectAndDecode(cv2.imread("info.jpg"))
print(val)# text

img=qrcode.make("https://www.linkedin.com/in/shouhardik/")
img.save("linkedin.jpg")