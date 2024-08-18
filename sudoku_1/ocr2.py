import cv2 
import easyocr

#read image
img = cv2.imread("./sdk2.png")
edged = cv2.Canny(img, 30, 200)
cv2.imshow("t", edged)
cv2.waitKey(0)
#instantiate the text detector 
reader = easyocr.Reader(['en'], gpu=False)

#read text on image
text = reader.readtext(edged)

#print text 

print(text[0][1])