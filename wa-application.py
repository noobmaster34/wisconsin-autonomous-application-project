
import cv2
import numpy as np

# im = cv2.imread("/Users/patrickwang/dev/cone-path/red.png") 
image = cv2.imread("red.png", cv2.IMREAD_COLOR)
cv2.imshow('original image', image)
cv2.waitKey(0)

# Define the red color range using BGR
lower_red = np.array([15, 14, 174]) # Lower range for red
upper_red = np.array([97, 93, 251]) # Upper range for red

# Create masks for red color (changes the red cone colors to white then makes everything else black), AKA thresholding
mask = cv2.inRange(image, lower_red, upper_red)
cv2.imshow('masked image', mask)
cv2.waitKey(0)

# Find contours in the mask
# cv2.RETR_EXTERNAL retrieves only the outermost contours
# cv2.CHAIN_APPROX_SIMPLE compresses the contours to save memory.
# the first output is list of countours
# the second output is the heiarchy of contours which we dont care about so we just use _ to discard the variable
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# list to store cone centers
cone_centers = []

# Filter and find the centers of the cones
for contour in contours: 
    if cv2.contourArea(contour) > 50: # if the contoured area is more than 50 pixels
        M = cv2.moments(contour) # calculates the spacial moments of the cone contour
        cx = int(M['m10'] / M['m00']) # x coordinate of the center of the cone contour
        cy = int(M['m01'] / M['m00']) # y coordinate of the center of the cone contour
        cone_centers.append((cx, cy)) # store the center coordinates into the list
        cv2.circle(image, (cx, cy), 5, (255, 255, 255), -1) # Draw a circle at the center of the cone on the original image at point (cx, cy)

# Sort the cones based on x-coordinates (left to right)
cone_centers.sort(key=lambda x: x[0])

# Split the cones into two categories based on x-coordinates
left_line = []
right_line = []

for center in cone_centers:
    if center[0] < image.shape[1] // 2: # check if the center is on the left side
        left_line.append(center) # add to left line list 
    else: 
        right_line.append(center)  #add to right line list

# Convert lists to NumPy arrays 
left_line = np.array(left_line)
right_line = np.array(right_line)

# Fit a line of best fit (linear regression) for left and right cones
if len(left_line) > 1:
    left_fit = np.polyfit(left_line[:, 1], left_line[:, 0], 1)  # Fit line for left
    left_line_y = np.array([min(left_line[:, 1]), max(left_line[:, 1])])  # Y-coordinates (top to bottom)
    left_line_x = left_fit[0] * left_line_y + left_fit[1]  # X-coordinates of the best fit line
    left_line_pts = np.column_stack((left_line_x, left_line_y)).astype(np.int32)
    cv2.polylines(image, [left_line_pts], isClosed=False, color=(0, 0, 255), thickness=2)

if len(right_line) > 1:
    right_fit = np.polyfit(right_line[:, 1], right_line[:, 0], 1)  # Fit line for right
    right_line_y = np.array([min(right_line[:, 1]), max(right_line[:, 1])])  # Y-coordinates (top to bottom)
    right_line_x = right_fit[0] * right_line_y + right_fit[1]  # X-coordinates of the best fit line
    right_line_pts = np.column_stack((right_line_x, right_line_y)).astype(np.int32)
    cv2.polylines(image, [right_line_pts], isClosed=False, color=(0, 0, 255), thickness=2)

# display the final image
cv2.imshow('Image with Detected Cones and Lines of Best Fit', image)
cv2.waitKey(0)
cv2.imwrite("answer.png", image)
cv2.destroyAllWindows()
