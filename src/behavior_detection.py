import time


class BehaviorDetector:
    def __init__(self, absence_seconds=3, movement_threshold=35, cooldown_seconds=5):
        self.absence_seconds = absence_seconds
        self.movement_threshold = movement_threshold
        self.cooldown_seconds = cooldown_seconds

        self.absence_started = None
        self.previous_center = None
        self.last_event = {}

    def _can_emit(self, event_name):
        now = time.time()
        last = self.last_event.get(event_name, 0)

        if now - last >= self.cooldown_seconds:
            self.last_event[event_name] = now
            return True

        return False

    def update(self, faces):
        events = []
        now = time.time()

        # No-face detection
        if len(faces) == 0:
            if self.absence_started is None:
                self.absence_started = now

            if now - self.absence_started >= self.absence_seconds:
                if self._can_emit("Face Absent"):
                    events.append(("Face Absent", 0))
        else:
            self.absence_started = None

        # Multiple-face detection
        if len(faces) > 1:
            if self._can_emit("Multiple Faces"):
                events.append(("Multiple Faces", len(faces)))

        # Basic movement analysis for one detected face
        if len(faces) == 1:
            x, y, w, h = faces[0]
            center = (x + w // 2, y + h // 2)

            if self.previous_center is not None:
                dx = abs(center[0] - self.previous_center[0])
                dy = abs(center[1] - self.previous_center[1])

                if dx + dy >= self.movement_threshold:
                    if self._can_emit("Head Movement"):
                        events.append(("Head Movement", 1))

            self.previous_center = center
        else:
            self.previous_center = None

        return events
