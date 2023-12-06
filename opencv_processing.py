import cv2
import numpy as np
import pyrealsense2 as rs

# Configurations for streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.yuyv, 6) # Was bgr8

# Start streaming
print("Starting the pipeline...")
pipeline.start(config)

# frame_skip_factor = 2

src = cv2.imread("canvasInput")
print(src.channels())

try:
	# frame_count = 0
	while True:

		# Wait for a coherent pair of frames: depth and color
		print("Waiting for frames...")
		# for index in range(5):
		# 	print("First wait loop")
		# 	pipeline.wait_for_frames()
		frames = pipeline.wait_for_frames()
		depth_frame = frames.get_depth_frame()
		color_frame = frames.get_color_frame()
		if not depth_frame or not color_frame:
			print("No depth or color frames received.")
			continue
		print("Frames received.")

		# Convert images to numpy arrays
		depth_image = np.asanyarray(depth_frame.get_data())
		color_image = np.asanyarray(color_frame.get_data())

		# if frame_count % frame_skip_factor == 0:
		# Convert YUYV to BGR
		# color_image = color_image.reshape((480, 640, 2))
		# color_image = cv2.cvtColor(color_image, cv2.COLOR_YUV2BGR_YUYV)
		# color_image = cv2.cvtColor(color_image, cv2.COLOR_YUV2RGB_YUYV)
		# color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB_BGR)

		# Convert BGR to HSV
		hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)


		# Define range of colors in HSV to target
		lower_brown = np.array([10, 100, 20])
		upper_brown = np.array([20, 255, 200])

		# Threshold the HSV image to get only brown colors
		mask = cv2.inRange(hsv, lower_brown, color_image)

		# Bitwise-AND the HSv image to get only desired colors
		res = cv2.bitwise_and(color_image, color_image, mask=mask)

		# Calculate "Moments" (Needed to compute centroid)
		M = cv2.moments(mask)
		if M["m00"] != 0:
			cX = int(M["m10"] / M["m00"])
			cY = int(M["m01"] / M["m00"])
		else:
			cX, cY = 0, 0

		# Get distance from depth frame
		dist = depth_frame.get_distance(cX, cY)

		print('Centroid coordinates: (', cX, ',', cY, ') Distance: ', dist, 'meters')
		# frame_count += 1

finally:

	# Stop streaming
	print("Stopping the pipeline...")
	pipeline.stop()
