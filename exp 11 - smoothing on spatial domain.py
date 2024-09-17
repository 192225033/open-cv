import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
kernel = np.ones((5, 5), np.float32) / 25
smoothed = cv2.filter2D(img, -1, kernel)
plt.imshow(cv2.cvtColor(smoothed, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
