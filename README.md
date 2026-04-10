# Intelligent Home Monitoring System - Lab 3

## Project Overview

This project implements a real-time intelligent home monitoring system using:
- **Laptop A (Camera Node)**: Captures video from webcam and streams it over the network using Flask
- **Laptop B (AI Node)**: Receives the video stream and runs YOLO object detection in real-time

---

## System Architecture

```
Laptop A (Camera)          Laptop B (AI Processing)
   ┌─────────────┐             ┌──────────────┐
   │  Webcam     │             │              │
   └──────┬──────┘             │              │
          │                    │              │
          │  Flask App         │              │
          │  (app.py)          │              │
          │                    │              │
   ┌──────▼──────────────────────────────────┐
   │  Network Stream (HTTP)                  │
   │  http://<IP>:5000/video_feed           │
   └─────────────────────────┬──────────────┘
                             │
                             │  YOLO Detection
                             │  (yolo_stream.py)
                             │
                             ▼
                      ┌──────────────┐
                      │ Bounding Box │
                      │ & Labels     │
                      └──────────────┘
```

---

## Requirements

### Software
- Python 3.8 or later
- Both laptops connected to the same WiFi network

### Dependencies

**Laptop A (Camera/Sender):**
```bash
pip install opencv-python flask
```

**Laptop B (AI Node/Receiver):**
```bash
pip install opencv-python ultralytics
```

---

## Setup Instructions

### Step 1: Verify Python Installation

On both laptops, run:
```bash
python --version
```

### Step 2: Install Dependencies

**On Laptop A:**
```bash
pip install opencv-python flask
```

**On Laptop B:**
```bash
pip install opencv-python ultralytics
```

### Step 3: Find Laptop A's IP Address

On Laptop A, open Command Prompt/PowerShell and run:
```bash
ipconfig
```

Look for the **IPv4 Address** under your WiFi network (usually looks like `192.168.x.x` or `10.x.x.x`)

Example: `10.214.13.1` *(this is your actual IP)*

### Step 4: Update the Stream URL

On Laptop B, edit `yolo_stream.py` and replace the IP address:
```python
STREAM_URL = "http://10.214.13.1:5000/video_feed"  # Replace with your Laptop A IP
```

---

## Running the System

### On Laptop A (Camera Node) - Terminal 1:

```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
```

The Flask server is now streaming video at port 5000.

### On Laptop B (AI Node) - Terminal 2:

```bash
python yolo_stream.py
```

You should see:
- Connection to the stream
- YOLO detections printed in console
- A window showing the video with bounding boxes around detected objects
- When a person is detected, the frame will be saved to `detections/` folder

---

## Testing Checklist

- [ ] Both laptops are on the same WiFi network
- [ ] Laptop A's `app.py` is running without errors
- [ ] Laptop B can connect to the stream URL
- [ ] YOLO model downloads and loads (first run takes ~100MB)
- [ ] Video window appears on Laptop B
- [ ] At least one object is detected and shown with bounding boxes
- [ ] Console shows detected object names and confidence scores
- [ ] Person detection frames are saved to `detections/` folder

---

## Features

### Core Features
✓ Real-time video streaming over network  
✓ Live YOLO object detection on incoming frames  
✓ Bounding boxes and labels on detected objects  
✓ Console output of detected objects with confidence scores  

### Bonus Features
✓ Automatic saving of frames when person is detected  
✓ Timestamped detection images in `detections/` folder  
✓ Multiple person detections tracked with counter  
✓ Graceful error handling and user feedback  

---

## Devices Used

| Role | Device | IP Address | Port | Model |
|------|--------|-----------|------|-------|
| Laptop A | Camera/Sender | 10.214.13.1 | 5000 | app.py |
| Laptop B | AI Node/Receiver | - | - | yolo_stream.py |

*Note: Actual IP used: 10.214.13.1 (obtained from `ipconfig`)*

---

## Detected Objects (YOLO v8n)

The YOLOv8 nano model can detect 80+ objects including:
- **People**: person
- **Vehicles**: car, truck, bicycle, motorcycle, etc.
- **Animals**: dog, cat, bird, horse, etc.
- **Household**: cup, bottle, chair, laptop, etc.

---

## Troubleshooting

### Issue: "Could not open stream"
**Solution:**
- Verify Laptop A's IP address is correct
- Make sure `app.py` is running on Laptop A
- Check if both laptops are on the same WiFi network
- Verify firewall isn't blocking port 5000

### Issue: "Could not open webcam" on Laptop A
**Solution:**
- Check if another application is using the webcam
- Try unplugging and replugging the camera
- Restart the app

### Issue: YOLO model downloading slowly
**Solution:**
- The model is ~100MB - first run takes time
- Ensure stable internet connection on Laptop B

### Issue: No detections appearing
**Solution:**
- Ensure there are objects in camera view
- Check YOLO is running (should see FPS in window title)
- Verify model loaded successfully in console

### Issue: Connection refused on Laptop B
**Solution:**
- Firewall blocking: Add Python to Windows Firewall exceptions
- Network isolation: Ensure same WiFi network
- Port conflict: Verify port 5000 is available

---

## Use Cases

This system demonstrates real-world applications:
1. **Smart Home Security**: Person detection for security alerts
2. **Baby Monitors**: Detect when baby wakes up or movement detected
3. **Warehouse Monitoring**: Detect inventory, people, equipment
4. **Wildlife Monitoring**: Detect specific animals in area
5. **Traffic Monitoring**: Detect vehicles and pedestrians

---

## Extension Ideas

1. **Send Alerts**: Email notification when person detected
2. **Log Detections**: Save detection data to database
3. **Multiple Classes**: Filter for specific object types only
4. **Performance Optimization**: Use lighter YOLO model (yolov8s, yolov8m)
5. **Recording**: Save video with annotations
6. **Multi-threaded**: Separate streaming and detection threads

---

## References

- [OpenCV Documentation](https://docs.opencv.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [YOLOv8 Docs](https://docs.ultralytics.com/)

---

## Lab Completion Status

- [x] Code files created (`app.py`, `yolo_stream.py`)
- [x] README with instructions
- [x] Dependencies fixed (NumPy 1.x compatibility)
- [x] Laptop A streaming successfully at 10.214.13.1:5000
- [x] Correct IP address verified and updated
- [ ] Screenshots captured (add images to `screenshots/` folder)
- [ ] Test run with proof

---

## Screenshots & Proof

Screenshots are saved in the `screenshots/` folder:

| Screenshot | Description |
|-----------|-------------|
| `laptop_a_flask_stream.png` | Flask streaming server running on Laptop A |
| `laptop_b_yolo_detection.png` | YOLO detection window showing bounding boxes |
| `detected_objects_console.png` | Console output showing detected objects |
| `person_detected_example.png` | Frame saved when person detected (bonus) |

### Expected Output Examples:

**Laptop A Console:**
```
 * Running on http://0.0.0.0:5000
 * Running on http://10.214.13.1:5000
Press CTRL+C to quit
```

**Laptop B Console:**
```
Stream opened. Running YOLO detection...
Detected: person (Confidence: 0.95)
✓ Person detected! Frame saved: detections/person_detected_01_20260410_120530.jpg
Detected: cup (Confidence: 0.87)
Detected: laptop (Confidence: 0.92)
```

---

---

## Notes

- The system runs at the hardware performance level of Laptop B
- Network latency may affect real-time performance
- For better performance, move closer to WiFi router
- First YOLO run will download the model (~100MB)

---

**Created for: Wireless and Radio Technology Lab 3**  
**Assignment Type: Pair Programming Lab**  
**Last Updated:** April 2026
