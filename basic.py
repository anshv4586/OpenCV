import cv2 as cv

img = cv.imread(r'C:\Users\ASUS\OneDrive\Desktop\deep learning\opencv\photo\cat.jpg')
cv.imshow('Cat', img)

# converting to grayscale
# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# blurring an image
# blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# edge cascade
# canny = cv.Canny(img , 125 , 175)
# cv.imshow('Canny Edges', canny)

# # Dilating the image
# dilated = cv.dilate(canny , (7,7) , iterations=3)
# cv.imshow('Dilated', dilated)

# # eroding the image
# eroded = cv.erode(dilated , (7,7) , iterations=3)
# cv.imshow('Eroded', eroded)

# resizing
resized = cv.resize(img , (500,500) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200 , 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)