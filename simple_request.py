import requests
import jsonpickle
import cv2

# initialize the REST API endpoint URL along with the input image path
REST_API_URL = "http://localhost:5000/funny"
IMAGE_PATH = "src/images/friends.jpg"
IMAGE_RESULT_PATH = "src/images/friends_result.png"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
r = requests.post(REST_API_URL, files=payload)#.json()

# Decode and save image received
frame = jsonpickle.decode(r.text)
frame_decoded = cv2.imdecode(frame, cv2.IMREAD_COLOR)
cv2.imwrite(IMAGE_RESULT_PATH, frame_decoded)