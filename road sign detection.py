from tensorflow.keras import models
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2
import h5py
import imutils
data = []
labels = []
classes = 43
classs = {1: "Speed limit (20km/h)",
          2: "Speed limit (30km/h)",
          3: "Speed limit (50km/h)",
          4: "Speed limit (60km/h)",
          5: "Speed limit (70km/h)",
          6: "Speed limit (80km/h)",
          7: "End of speed limit (80km/h)",
          8: "Speed limit (100km/h)",
          9: "Speed limit (120km/h)",
          10: "No passing",
          11: "No passing veh over 3.5 tons",
          12: "Right-of-way at intersection",
          13: "Priority road",
          14: "Yield",
          15: "Stop",
          16: "No vehicles",
          17: "Veh > 3.5 tons prohibited",
          18: "No entry",
          19: "General caution",
          20: "Dangerous curve left",
          21: "Dangerous curve right",
          22: "Double curve",
          23: "Bumpy road",
          24: "Slippery road",
          25: "Road narrows on the right",
          26: "Road work",
          27: "Traffic signals",
          28: "Pedestrians",
          29: "Children crossing",
          30: "Bicycles crossing",
          31: "Beware of ice/snow",
          32: "Wild animals crossing",
          33: "End speed + passing limits",
          34: "Turn right ahead",
          35: "Turn left ahead",
          36: "Ahead only",
          37: "Go straight or right",
          38: "Go straight or left",
          39: "Keep right",
          40: "Keep left",
          41: "Roundabout mandatory",
          42: "End of no passing",
          43: "End no passing veh > 3.5 tons"}
print("Loading Model...")
model = load_model("my_model.h5", compile=False)
print("Model Loaded!")
Loading Model...
Model Loaded!
print("Starting Camera...")
cam = cv2.VideoCapture(0)

while True:
    frame = cam.read()[1]
    img = Image.fromarray(frame, "RGB")
    img = img.resize((30, 30))
    img = np.expand_dims(img, axis=0)
    img = np.array(img)

    result = model.predict_classes(img)[0]
    sign = classs[result + 1]
    print("The sign says: ", sign)

    cv2.putText(frame, sign, (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0, 0, 255), 1)
    frame = imutils.resize(frame, width=500)
    cv2.imshow("Caputering", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
Starting Camera...
c:\users\achin\appdata\local\programs\python\python36\lib\site-packages\tensorflow\python\keras\engine\sequential.py:450: UserWarning: `model.predict_classes()` is deprecated and will be removed after 2021-01-01. Please use instead:* `np.argmax(model.predict(x), axis=-1)`,   if your model does multi-class classification   (e.g. if it uses a `softmax` last-layer activation).* `(model.predict(x) > 0.5).astype("int32")`,   if your model does binary classification   (e.g. if it uses a `sigmoid` last-layer activation).
  warnings.warn('`model.predict_classes()` is deprecated and '
The sign says:  Roundabout mandatory
The sign says:  Right-of-way at intersection
The sign says:  Double curve
The sign says:  No passing veh over 3.5 tons
The sign says:  No passing veh over 3.5 tons
The sign says:  Double curve
The sign says:  No passing veh over 3.5 tons
The sign says:  No passing veh over 3.5 tons
The sign says:  No passing veh over 3.5 tons
The sign says:  Double curve
The sign says:  Double curve
The sign says:  Double curve
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Bicycles crossing
The sign says:  Bicycles crossing
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (120km/h)
The sign says:  Speed limit (120km/h)
The sign says:  No passing
The sign says:  No passing
The sign says:  No passing veh over 3.5 tons
The sign says:  No passing veh over 3.5 tons
The sign says:  Dangerous curve right
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Double curve
The sign says:  Wild animals crossing
The sign says:  Wild animals crossing
The sign says:  Keep left
The sign says:  Keep left
The sign says:  Bumpy road
The sign says:  Bumpy road
The sign says:  Bumpy road
The sign says:  Bumpy road
The sign says:  Bumpy road
The sign says:  General caution
The sign says:  General caution
The sign says:  General caution
The sign says:  General caution
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  Road work
The sign says:  General caution
The sign says:  Road work
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Road work
The sign says:  Beware of ice/snow
The sign says:  Road work
The sign says:  Road work
The sign says:  Road work
The sign says:  Road work
The sign says:  Road work
The sign says:  Road work
The sign says:  Road work
The sign says:  Road work
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  No vehicles
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  Yield
The sign says:  Road work
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Road work
The sign says:  Yield
The sign says:  Keep right
The sign says:  Speed limit (120km/h)
The sign says:  Wild animals crossing
The sign says:  Speed limit (60km/h)
The sign says:  General caution
The sign says:  Road work
The sign says:  Road work
The sign says:  End of speed limit (80km/h)
The sign says:  End of speed limit (80km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Dangerous curve right
The sign says:  Dangerous curve right
The sign says:  Right-of-way at intersection
The sign says:  Right-of-way at intersection
The sign says:  Speed limit (30km/h)
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Stop
The sign says:  Dangerous curve right
The sign says:  Dangerous curve right
The sign says:  Bicycles crossing
The sign says:  Bicycles crossing
The sign says:  Stop
The sign says:  Stop
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  Speed limit (30km/h)
The sign says:  General caution
The sign says:  General caution
The sign says:  Bumpy road
The sign says:  Bumpy road
The sign says:  Bicycles crossing
The sign says:  Bicycles crossing
The sign says:  End of speed limit (80km/h)
The sign says:  Traffic signals
The sign says:  Traffic signals
The sign says:  General caution
The sign says:  General caution
The sign says:  Road work
The sign says:  Road work
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Yield
The sign says:  Bumpy road
The sign says: 
 
