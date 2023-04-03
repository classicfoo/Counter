import cv2

# Load the image
image = cv2.imread('drawing.jpg')

# Define the scale factor for zooming
scale_factor = 1.0

# Define the size of the circle
circle_size = 20

# Define the mouse callback function
def mouse_callback(event, x, y, flags, param):
    global scale_factor, image, circle_size, circle_count, circle_color, label_text

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

        # Display the resized image with the circle count
        count_text = f"{label_text}{circle_count}"
        cv2.putText(image_resized, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, circle_color, 2)
        cv2.imshow('Drawing', image_resized)

    # Draw a colored circle on left click
    elif event == cv2.EVENT_LBUTTONDOWN:
        # Calculate the position of the circle based on the resized image
        x_resized, y_resized = int(x / scale_factor), int(y / scale_factor)

        cv2.circle(image, (x_resized, y_resized), circle_size, circle_color, -1)

        # Increment the circle count
        circle_count += 1

        # Display the resized image with the circle count
        h, w = image.shape[:2]
        new_h, new_w = int(h * scale_factor), int(w * scale_factor)
        image_resized = cv2.resize(image, (new_w, new_h))
        count_text = f"{label_text}{circle_count}"
        cv2.putText(image_resized, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, circle_color, 2)
        cv2.imshow('Drawing', image_resized)

# Initialize the circle count to 0
circle_count = 0

# Set the circle color and label text
circle_color = (0, 0, 255)  # Red
# circle_color = (0, 255, 0)  # Green
# circle_color = (255, 0, 0)  # Blue
# circle_color = (0, 255, 255)  # Yellow
# circle_color = (0, 128, 255)  # Orange
# circle_color = (255, 0, 255)  # Purple

label_text = "Total Count: "

# Display the image with the circle count
h, w = image.shape[:2]
image_resized = cv2.resize(image, (w, h))
count_text = f"{label_text}{circle_count}"
cv2.putText(image_resized, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, circle_color, 2)
cv2.imshow('Drawing', image_resized)

# Register the mouse callback function
cv2.setMouseCallback('Drawing', mouse_callback)

# Wait for a key press
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()