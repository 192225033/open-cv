from PIL import Image

# Load the image
image_path = "C:\\Users\\HP\\Pictures\\Saved Pictures\\Capture.PNG"  # Use double backslashes
image = Image.open(image_path)

# Convert the image to grayscale
gray_image = image.convert("L")

# Show the original and grayscale images
image.show()          # Displays the original image
gray_image.show()     # Displays the grayscale image





