import cv2

# Load your MRI image
image = cv2.imread('C:\\Users\\S M FAHAD JAAN\\OneDrive\\Desktop\\BTD\\pred\\pred7.jpg', 0)  # Load the image in grayscale mode

# Apply CLAHE to enhance contrast
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # You can adjust clipLimit as needed
enhanced_image = clahe.apply(image)

# Save the preprocessed image
cv2.imwrite('enhanced_mri_image.jpg', enhanced_image)

# You can also display the original and enhanced images for visual comparison
cv2.imshow('Original MRI Image', image)
cv2.imshow('Enhanced MRI Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
