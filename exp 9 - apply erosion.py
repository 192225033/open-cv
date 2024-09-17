import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)
plt.imshow(eroded, cmap='gray')
plt.title('Erosion')
plt.axis('off')
plt.show()
