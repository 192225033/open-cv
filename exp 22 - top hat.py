import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg', 0)
kernel = np.ones((5, 5), np.uint8)
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
top_hat = cv2.subtract(img, opened)
plt.imshow(top_hat, cmap='gray')
plt.title('Top Hat')
plt.axis('off')
plt.show()
