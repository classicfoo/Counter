import cv2

# Load the image
image = cv2.imread('drawing.jpg')

# Define the scale factor for zooming
scale_factor = 1.0

# Define the size of the circle
circle_size = 20

# Define the mouse callback function
def mouse_callback(event, x, y, flags, param):
    global scale_factor, image, circle_size

    # Zoom in/out on Ctrl+Scroll
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            scale_factor *= 1.1
        else:
            scale_factor /= 1.1

        # Apply the zoom factor to the image
        h, w = image.shape[:2]
        new_h, new_w = int(h * scale_factor), int(w * scale_factor)
        image_resized = cv2.resize(image, (new_w, new_h))

        # Display the resized image
        cv2.imshow('Drawing', image_resized)

    # Draw a red circle on left click
    elif event == cv2.EVENT_LBUTTONDOWN:
        # Calculate the position of the circle based on the resized image
        x_resized, y_resized = int(x / scale_factor), int(y / scale_factor)

        cv2.circle(image, (x_resized, y_resized), circle_size, (0, 0, 255), -1)

        # Display the resized image
        h, w = image.shape[:2]
        new_h, new_w = int(h * scale_factor), int(w * scale_factor)
        image_resized = cv2.resize(image, (new_w, new_h))
        cv2.imshow('Drawing', image_resized)

# Display the image
cv2.imshow('Drawing', image)

# Register the mouse callback function
cv2.setMouseCallback('Drawing', mouse_callback)

# Wait for a key press
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()
