import cv2, numpy as np, matplotlib.pyplot as plt
img = cv2.imread('C:\\Users\\deves\\Downloads\\CV IMAGES\\images.jpeg', 0)
prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
edge_x = cv2.filter2D(img, -1, prewitt_x)
edge_y = cv2.filter2D(img, -1, prewitt_y)
prewitt = cv2.magnitude(edge_x, edge_y)
plt.imshow(prewitt, cmap='gray')
plt.show()