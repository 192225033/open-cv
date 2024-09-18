import cv2, matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg', 0)
canny = cv2.Canny(img, 100, 200)
plt.imshow(canny, cmap='gray')
plt.show()
