import json, random, time
from faker import Faker
from datetime import datetime

fake = Faker()

ACTIONS = ["play", "pause", "skip", "completed"]
DEVICES = ["mobile", "desktop", "tablet", "web"]
LOCATIONS = ["USA", "Canada", "UK", "Germany", "France", "Australia"]
VERSIONS = ["1.0", "1.1", "2.0", "2.1"]


def generate_event():
    """
    Generate a random event simulating a user interaction with music streaming service.

    Returns:
        dict: A dictionary containing event details including user_id, action, device, location, version, and timestamp.
    """
    event = {
        "user_id": fake.uuid4(),
        "action": random.choice(ACTIONS),
        "device": random.choice(DEVICES),
        "location": random.choice(LOCATIONS),
        "version": random.choice(VERSIONS),
        "timestamp": datetime.now().isoformat(),
    }
    return event


if __name__ == "__main__":
    while True:
        event = generate_event()
        print(json.dumps(event))
        time.sleep(1)  # Delay event generation by 1 second
