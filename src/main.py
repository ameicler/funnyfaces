from PIL import Image
import numpy as np
from flask import Flask, request, Response
import io
import cv2
from detect import img_to_array, funny_face
import jsonpickle

# initialize our Flask application and the Keras model
app = Flask(__name__)
model = None


def prepare_image(image, target):
	# resize the input image and preprocess it
	if target is not None:
		image = image.resize(target)
	image = img_to_array(image).astype(np.uint8)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# return the processed image
	return image

@app.route("/funny", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if request.method == "POST":
		if request.files.get("image"):
			# read the image in PIL format
			image = request.files["image"].read()
			image = Image.open(io.BytesIO(image))

			# preprocess the image
			image = prepare_image(image, target=None) #(224, 224))
			funny_face_arr = funny_face(image)
			#cv2.imwrite('images/image_overlay.png', funny_face_img)

			# return the image without saving temporary
			_, funny_face_frame = cv2.imencode('.jpg', funny_face_arr)
			response_pickled = jsonpickle.encode(funny_face_frame)
			return Response(response=response_pickled, status=200, mimetype="application/json")

# Start the server
if __name__ == "__main__":
	app.run(host="0.0.0.0")