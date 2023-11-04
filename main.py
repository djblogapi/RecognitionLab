import cv2
import face_recognition

CAMERA_ID = "/dev/video0"

cap = cv2.VideoCapture(CAMERA_ID)

face_locations = []

make_screenshot = True

while True:
	# Grab a single frame of video
	ret, frame = cap.read()
	# Convert the image from BGR color (which OpenCV uses) to RGB
	# color (which face_recognition uses)
	rgb_frame = frame[:, :, ::-1]
	# Find all the faces in the current frame of video
	face_locations = face_recognition.face_locations(rgb_frame)
	if face_locations:
		# TODO send screen to web server (temporary make one screen and save it)
		if make_screenshot:
			cv2.imwrite("screenshot.jpeg", frame)
			make_screenshot = False
		for top, right, bottom, left in face_locations:
			# Draw a box around the face
			cv2.rectangle(frame, (left, top), (right, bottom), (159, 237, 164), 2)

	# Display the resulting image
	cv2.imshow('Video', frame)

	# Wait for Enter key to stop
	if cv2.waitKey(25) == 13:
		break
