import cv2
import numpy as np
import matplotlib.pyplot as plt

# Open the video file
cap = cv2.VideoCapture('video.mp4')

# Initialize the background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=15, detectShadows=False)

# Initialize variables to store previous and current centroid coordinates
prev_centroid = None
curr_centroid = None

# Initialize variables to calculate velocity and acceleration
prev_velocity = None
curr_velocity = None
prev_acceleration = None
distances = []
velocities = []
accelerations = []

while True:
    # Read a new frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction
    fgmask = fgbg.apply(frame)
    
    # Apply morphological operations to remove noise
    kernel = np.ones((12,1),np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    
    # Find contours in the foreground mask
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the contour with the largest area
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour
    
    if max_contour is not None:
        # Draw a bounding box around the car
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 255, 0), 2)

        # Calculate the centroid of the bounding box
        curr_centroid = (x + w // 2, y + h // 2)

        # Draw the centroid on the frame
        cv2.circle(frame, curr_centroid, 5, (0, 10, 200), -1)

        # Calculate velocity and acceleration
        if prev_centroid is not None:
            curr_velocity = ((curr_centroid[0] - prev_centroid[0]) / 10, (curr_centroid[1] - prev_centroid[1]) / 10)
            if prev_velocity is not None:
                prev_acceleration = ((curr_velocity[0] - prev_velocity[0]) / 10, (curr_velocity[1] - prev_velocity[1]) / 10)

            # Calculate distance between previous and current centroid
            distance = np.sqrt((curr_centroid[0] - prev_centroid[0])**2 + (curr_centroid[1] - prev_centroid[1])**2)
            distances.append(distance)

            # Store velocity and acceleration for plotting
            velocities.append(np.linalg.norm(curr_velocity))
            
            if prev_velocity is not None and prev_acceleration is not None:
                acceleration_norm = np.linalg.norm(prev_acceleration)
                accelerations.append(acceleration_norm)
            else:
                accelerations.append(0)

        # Store current centroid as previous centroid for next iteration
        prev_centroid = curr_centroid
        prev_velocity = curr_velocity

    # Display the frame
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()



# Plot distance, velocity, and acceleration
fig, axs = plt.subplots(3, 1, figsize=(8, 10))
fig.suptitle('Distance, Velocity, and Acceleration over Time')
fig.subplots_adjust(hspace=0.6)

# Plot distance
axs[0].plot(distances)
axs[0].set_title('Distance')
axs[0].set_ylabel('Distance (pixels)')

# Plot velocity
axs[1].plot(velocities)
axs[1].set_title('Velocity')
axs[1].set_ylabel('Velocity (pixels/frame)')

# Plot acceleration
axs[2].plot(accelerations)
axs[2].set_title('Acceleration')
axs[2].set_xlabel('Frame')
axs[2].set_ylabel('Acceleration (pixels/frame^2)')

# Show the plot
plt.show()


