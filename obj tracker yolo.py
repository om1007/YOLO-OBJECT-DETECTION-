
# CONTOURS DETECTION 

import os
import cv2

img = cv2.imread(r"C:\Users\om\Desktop\CV\i.png")

img_gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)


# Contours detect the ite spaces in the img 
ret, thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Count the number of contours
num_contours = len(contours)

#finding all outlines in img > 200 & draving rect around them 
for cnt in contours:
    print(cv2.contourArea(cnt))

    if cv2.contourArea(cnt) > 1800: 
      # dravs outline on all objects present in  original image 
    #  cv2.drawContours(img, cnt,-1,(0,255,0))
    
        x1,y1 , w,h = cv2.boundingRect(cnt) 

    cv2.rectangle(img, (x1,y1), (x1 + w, y1 + h), (0,255,0),2) 

# Display the number of contours using cv2.putText
cv2.putText(img, f"Contours: {num_contours - 1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
while True:
    cv2.imshow("img", img)
    
    # cv2.imshow("img_gray", img_gray)
    # cv2.imshow("thresh", thresh)
    if cv2.waitKey(1) == ord('q'):  # Check for 'q' press every 1ms
        break

cv2.destroyAllWindows()
