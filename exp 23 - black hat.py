import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg', 0)
kernel = np.ones((5, 5), np.uint8)
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
black_hat = cv2.subtract(closed, img)
plt.imshow(black_hat, cmap='gray')
plt.title('Black Hat')
plt.axis('off')
plt.show()
