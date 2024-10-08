import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('C:\\Users\\deves\\Downloads\\CV IMAGES\\images.jpeg', 0)
roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
edge_x = cv2.filter2D(img, cv2.CV_32F, roberts_x)
edge_y = cv2.filter2D(img, cv2.CV_32F, roberts_y)
roberts = cv2.magnitude(edge_x, edge_y)
plt.imshow(roberts, cmap='gray')
plt.show()
