import cv2
import face_recognition
cap = cv2.VideoCapture("/dev/video0")

face_locations = []
flag = True
while True:
	# Grab a single frame of video
	ret, frame = cap.read()
	# Convert the image from BGR color (which OpenCV uses) to RGB
	# color (which face_recognition uses)
	rgb_frame = frame[:, :, ::-1]
	# Find all the faces in the current frame of video
	face_locations = face_recognition.face_locations(rgb_frame)
	for top, right, bottom, left in face_locations:
		# Draw a box around the face
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

	# Display the resulting image
	cv2.imshow('Video', frame)
	if flag:
		cv2.imwrite("test.jpg", frame)
		flag = False
	# Wait for Enter key to stop
	if cv2.waitKey(25) == 13:
		break

