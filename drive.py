import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2
 
sio = socketio.Server()
 
app = Flask(__name__) #'__main__'
speed_limit = 10
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img
 
@sio.on('connect')
def connect(sid, environ):
    print(f'Connected: {sid}')
    send_control(0, 0)
 
def send_control(steering_angle, throttle):
    print(f"Sending control - Steering Angle: {steering_angle}, Throttle: {throttle}")
    sio.emit('steer', data={
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        speed = float(data['speed'])
        print(f"Speed: {speed}")

        # Decode image from base64
        imgString = data['image']
        image = Image.open(BytesIO(base64.b64decode(imgString)))
        image = np.asarray(image)
        print("Image received and converted to array.")

        # Preprocess the image
        image = img_preprocess(image)
        print("Image preprocessed.")
        
        # Prepare image for prediction
        image = np.array([image])
        print(f"Image shape for prediction: {image.shape}")

        # Predict steering angle
        steering_angle = float(model.predict(image))
        print(f"Predicted steering angle: {steering_angle}")

        # Calculate throttle
        throttle = 1.0 - speed/speed_limit 
        print(f"Calculated throttle: {throttle}")

        # Send control commands
        send_control(steering_angle, throttle)
    else:
        print("No data received")
 

 
 
if __name__ == '__main__':
    model = load_model('./models/model-3.h5')
    print("Model loaded successfully.")
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)