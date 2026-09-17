import cv2

from src.config import (
    ABSENCE_SECONDS,
    MOVEMENT_THRESHOLD,
    EVENT_COOLDOWN_SECONDS,
)
from src.face_detection import FaceDetector
from src.behavior_detection import BehaviorDetector
from src.event_logger import EventLogger


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Unable to access the webcam.")

    detector = FaceDetector()
    behavior = BehaviorDetector(
        absence_seconds=ABSENCE_SECONDS,
        movement_threshold=MOVEMENT_THRESHOLD,
        cooldown_seconds=EVENT_COOLDOWN_SECONDS,
    )
    logger = EventLogger("logs/events.csv")

    print("AI-Based Cheating Detection System started.")
    print("Press 'q' to exit.")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("Unable to read a webcam frame.")
            break

        faces = detector.detect(frame)
        events = behavior.update(faces)

        for event_name, detail in events:
            logger.log(event_name, detail)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if len(faces) == 0:
            status = "NO FACE DETECTED"
        elif len(faces) > 1:
            status = f"MULTIPLE FACES: {len(faces)}"
        else:
            status = "MONITORING"

        cv2.putText(
            frame,
            status,
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255) if len(faces) != 1 else (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            "Press Q to exit",
            (20, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1,
        )

        cv2.imshow("AI Cheating Detection System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
