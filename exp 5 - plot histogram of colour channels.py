import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\images.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for i, color in enumerate(['r', 'g', 'b']):
    plt.plot(cv2.calcHist([img_rgb], [i], None, [256], [0, 256]), color=color)
plt.title('Color Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
