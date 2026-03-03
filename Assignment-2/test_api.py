import requests
import json

BASE_URL = "http://127.0.0.1:8000/events/"

def test_events_api():
    # 1. Create Event
    print("Testing Create Event...")
    payload = {
        "name": "Magic Party",
        "description": "Fun times at the castle",
        "location": "Hogwarts",
        "start_date": "2025-01-01T10:00:00Z",
        "end_date": "2025-01-01T12:00:00Z"
    }
    response = requests.post(BASE_URL + "create/", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code != 201:
        return
    
    event_id = response.json().get("id")

    # 2. Get All Events
    print("\nTesting Get All Events...")
    response = requests.get(BASE_URL)
    print(f"Status: {response.status_code}")
    print(f"First event: {response.json()[0] if response.json() else 'None'}")

    # 3. Get Single Event
    print(f"\nTesting Get Single Event ({event_id})...")
    response = requests.get(BASE_URL + f"{event_id}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # 4. Update Event (PATCH)
    print(f"\nTesting Update Event ({event_id})...")
    patch_payload = {"location": "Diagon Alley"}
    response = requests.patch(BASE_URL + f"{event_id}/update/", json=patch_payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # 5. Delete Event
    print(f"\nTesting Delete Event ({event_id})...")
    response = requests.delete(BASE_URL + f"{event_id}/delete/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_events_api()
