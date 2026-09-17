# AI-Based Cheating Detection System

A computer-vision-based examination monitoring prototype that analyzes webcam video in real time and flags potentially suspicious events for human review.

> **Important:** This project is a monitoring aid, not a system that can conclusively determine whether cheating occurred. Detection events can have false positives and should be reviewed by a human.

## Features

- Real-time webcam monitoring
- Face detection using OpenCV
- Multiple-face detection
- Candidate-absence detection
- Basic head-position/movement analysis
- On-screen event notifications
- Timestamped CSV event logging
- Configurable detection thresholds
- Simple modular project structure

## Detection Workflow

```text
Webcam
   |
   v
Frame Capture
   |
   v
Face Detection
   |
   +--> No Face --------> Absence Event
   |
   +--> Multiple Faces -> Multiple-Face Event
   |
   +--> One Face ------> Head Movement Analysis
                              |
                              v
                         Event Logger
```

## Technology Stack

- Python 3.10+
- OpenCV
- NumPy
- PyTest

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/AI-Cheating-Detection-System.git
cd AI-Cheating-Detection-System

python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The application opens the default webcam.

Press `q` to exit.

Events are saved to:

```text
logs/events.csv
```

## Detection Logic

### No Face

If no face is detected continuously for the configured absence interval, an absence event is recorded.

### Multiple Faces

If more than one face is detected, a multiple-face event is recorded.

### Head Movement

For a single detected face, the system tracks the movement of the face bounding-box center. Sustained movement beyond the configured threshold can generate a head-movement event.

This is intentionally a lightweight demonstration rather than a medical-grade or production-grade pose-estimation model.

## Configuration

Detection parameters can be changed in `src/config.py`:

```python
ABSENCE_SECONDS = 3
MOVEMENT_THRESHOLD = 35
EVENT_COOLDOWN_SECONDS = 5
```

## Example Events

```text
2026-09-18 10:30:12,Multiple Faces,2
2026-09-18 10:31:04,Face Absent,0
2026-09-18 10:32:18,Head Movement,1
```

## Project Structure

```text
AI-Cheating-Detection-System/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── face_detection.py
│   ├── behavior_detection.py
│   └── event_logger.py
├── screenshots/
├── logs/
│   └── .gitkeep
└── tests/
    └── test_detection.py
```

## Limitations

- Webcam quality affects detection accuracy.
- Lighting and camera angle can produce false positives.
- Face detection alone cannot determine intent.
- Head movement is only a basic proxy for potentially unusual behavior.
- Events should be reviewed before any academic or disciplinary decision.

## Future Improvements

- Face recognition for candidate verification
- MediaPipe/YOLO-based pose estimation
- Gaze estimation
- Object detection for prohibited items
- Web dashboard for reviewing events
- Encrypted evidence storage
- Role-based access control
- Database-backed event management

## Ethical Considerations

Exam-monitoring systems involve sensitive video and behavioral information. A real deployment should use informed consent, data minimization, appropriate retention policies, access controls, and applicable privacy regulations.

## Author

**Krishnadev JS**

Cybersecurity | Network Security | Ethical Hacking | Computer Vision
