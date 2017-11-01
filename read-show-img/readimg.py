# reading and displaying image
import numpy as np
import cv2

# Load color image in grayscale
img = cv2.imread('fredrogers.jpeg', 0)

# Display img
cv2.imshow('image', img)

# Close image on 0 Key
cv2.waitKey(0)
cv2.destroyAllWindows()
