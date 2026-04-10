import cv2
from ultralytics import YOLO
import os
from datetime import datetime

# Replace with the actual IP address of Laptop A (Camera node)
STREAM_URL = "http://192.168.1.20:5000/video_feed"

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print("Error: Could not open stream.")
    print(f"Make sure Laptop A is running app.py and the URL is correct: {STREAM_URL}")
    exit()

print("Stream opened. Running YOLO detection...")
print("Press 'q' to quit")

# Create directory for saving person detection frames
if not os.path.exists("detections"):
    os.makedirs("detections")

person_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    # Check for detected objects
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = result.names[class_id]
            confidence = float(box.conf)
            
            print(f"Detected: {class_name} (Confidence: {confidence:.2f})")
            
            # Bonus: Save frame when person is detected
            if class_name == "person":
                person_count += 1
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"detections/person_detected_{person_count:02d}_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"✓ Person detected! Frame saved: {filename}")

    cv2.imshow("YOLO Home Monitoring", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Program closed.")
