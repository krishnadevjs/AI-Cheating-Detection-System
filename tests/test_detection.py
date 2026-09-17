from src.behavior_detection import BehaviorDetector


def test_multiple_face_event():
    detector = BehaviorDetector(cooldown_seconds=0)

    faces = [
        (10, 10, 100, 100),
        (200, 10, 100, 100),
    ]

    events = detector.update(faces)

    assert any(name == "Multiple Faces" for name, _ in events)


def test_single_face_has_no_multiple_face_event():
    detector = BehaviorDetector(cooldown_seconds=0)

    events = detector.update([(10, 10, 100, 100)])

    assert not any(name == "Multiple Faces" for name, _ in events)
