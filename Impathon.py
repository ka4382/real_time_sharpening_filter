import cv2
import numpy as np

# Load the input image (simulating a frame from a video)
image = cv2.imread('image.png')
image = cv2.resize(image, (640, 480))  # Resize for real-time performance

# Define a sharpening kernel
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_color = (255, 255, 255)   # White text
thickness = 2
bg_color = (0, 0, 0)  # Black background for label

# Real-time simulation loop
while True:
    # Apply sharpening filter
    sharpened = cv2.filter2D(image, -1, sharpen_kernel)

    # Add label to original image
    original_label = image.copy()
    cv2.rectangle(original_label, (10, 30), (140, 60), bg_color, -1)  # Label background
    cv2.putText(original_label, "Original", (15, 55), font, font_scale, font_color, thickness)

    # Add label to sharpened image
    sharpened_label = sharpened.copy()
    cv2.rectangle(sharpened_label, (10, 30), (160, 60), bg_color, -1)  # Label background
    cv2.putText(sharpened_label, "Sharpened", (15, 55), font, font_scale, font_color, thickness)

    # Combine side-by-side
    combined = np.hstack((original_label, sharpened_label))
    cv2.imshow("Real-Time Sharpening: Original vs Sharpened", combined)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
