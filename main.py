from datetime import datetime, timedelta
import json
import cv2
import face_recognition
import requests
from mqtt import client
# setup camera id
CAMERA_ID = "/dev/video0"

# cap = cv2.VideoCapture(CAMERA_ID)
cap = cv2.VideoCapture('video.mp4')

# Setup api url for requests
URL = "http://localhost/v1/users/file/"

face_locations = []
screenshot_timestamp = datetime.now()

while True:
    # Grab a single frame of video
    ret, frame = cap.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB
    # color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]
    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    if face_locations:
        for top, right, bottom, left in face_locations:
            if screenshot_timestamp < datetime.now():
                screenshot_timestamp = datetime.now() + timedelta(seconds=5)
                imencoded = cv2.imencode(".jpg", frame)[1]
                # send data to mqtt
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                # raise Exception(type(face_encodings))
                # Loop through each face found in the image
                for i, face_encoding in enumerate(face_encodings):
                    # Convert face encoding to bytes for database storage
                    message = list(face_encoding)
                    client.publish('face_recognition', json.dumps(message))
                # send image to django app
                data = {'image': ('face.jpg', imencoded.tobytes(), 'image/jpeg')}
                try:
                    resp = requests.post(URL, files=data)
                except Exception as e:
                    # Log error
                    print(e)
            # Draw a box around the face
            cv2.rectangle(frame, (left - 20, top - 20), (right + 20, bottom + 20), (0, 0, 255), 2)
            cv2.imwrite("test1.jpg", frame)
        # time.sleep(10)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Wait for Enter key to stop
    if cv2.waitKey(25) == 13:
        break
