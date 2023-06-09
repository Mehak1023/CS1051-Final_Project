# CS1051-Final_Project
Object Tracking in Python: Create a system that can track the movement of objects within a sequence of images or video, such as tracking the movement of vehicles or people.
Throughout the project, I struggled with object recognition and classification; as I did more research, I realized most robust tracking algorithms are heavily based on machine learning, which I need more time to learn. I tried to employ already created tracker alogothims like YOLOV5, but unfortunately, I struggled with downloading and setting up those programs into IDLE. Then I tried using the auto tracker features in openCV, such as cv2.TrackerKCF_create(); however, I always got an error that it was not a valid module in the openCV toolbox. Finally, I checked the version of cv2, 4.7.0, so it should have worked, but it was not working. Therefore, I manually wrote the code for tracking an object in a video and calculating its velocity and acceleration. I  experimented with different values to adjust the background subtractor's parameters and morphological operations. I saw how they affect the performance of the tracking algorithm and learned how to experiment with other features in openCV.

The "history" parameter determines how many previous frames are used to build the background model for the background subtractor. A larger value will result in a more accurate background model but may also be more computationally expensive. The "varThreshold" parameter controls the threshold for classifying pixels as foreground or background. A lower value will result in more pixels being classified as foreground, which may help detect small or fast-moving objects. However, it may also result in more noise in the foreground mask.

The size and shape of the kernel used for erosion and dilation can be adjusted for morphological operations. For example, a more prominent grain will smooth the foreground mask but may also lose detail. The shape of the kernel can also be changed depending on the specific characteristics of the foreground mask in your video. It's best to start with the default parameters and gradually adjust them until you achieve the desired results. You can also try different combinations of parameters to find the optimal configuration for your specific video.

I chose a car commercial with varying speeds and locations in the frame, which made the tracking harder, and I tried my best to play with the physical parameters for monitoring. Overall, I am not greatly happy with the result, but I enjoyed learning more about the openCV toolbox in Python. I could use it much better for a more accessible guided video when I need it in future experiments. 

Code and video are uploaded in GITHUB

Link to video: https://clipchamp.com/watch/b6HO7X1h18h


