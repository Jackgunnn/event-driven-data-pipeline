import random
import uuid
import time
from datetime import datetime, UTC

EVENT_TYPES = [
    "question_posted",
    "answer_posted",
    "question_upvoted",
    "answer_upvoted",
    "question_downvoted",
    "answer_downvoted",
    "question_deleted",
    "answer_deleted",
    "question_edited",
    "answer_edited",
]


def generate_event():
    event_type = random.choice(EVENT_TYPES)

    event = {
        "event_id": str(uuid.uuid4()),
        "event_version": 1,
        "event_type": event_type,
        "source": "discuzz-forum-app",
        "user_id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat()
    }

    if event_type == "question_posted":
        event["question_id"] = str(uuid.uuid4())

    elif event_type == "answer_posted":
        event["question_id"] = str(uuid.uuid4())
        event["answer_id"] = str(uuid.uuid4())

    elif event_type == "question_upvoted":
        event["question_id"] = str(uuid.uuid4())

    elif event_type == "answer_upvoted":
        event["question_id"] = str(uuid.uuid4())
        event["answer_id"] = str(uuid.uuid4())

    elif event_type == "question_downvoted":
        event["question_id"] = str(uuid.uuid4())

    elif event_type == "answer_downvoted":
        event["question_id"] = str(uuid.uuid4())
        event["answer_id"] = str(uuid.uuid4())

    elif event_type == "question_deleted":
        event["question_id"] = str(uuid.uuid4())

    elif event_type == "answer_deleted":
        event["question_id"] = str(uuid.uuid4())
        event["answer_id"] = str(uuid.uuid4())

    elif event_type == "question_edited":
        event["question_id"] = str(uuid.uuid4())

    elif event_type == "answer_edited":
        event["question_id"] = str(uuid.uuid4())
        event["answer_id"] = str(uuid.uuid4())

    return event


if __name__ == "__main__":
    while True:
        print(generate_event())
        time.sleep(1)
    
