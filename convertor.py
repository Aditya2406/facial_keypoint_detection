import cv2
originalImage = cv2.imread('test_2.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
img="test02_bw.jpg"
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Gray image', grayImage)
cv2.imwrite(img,grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()