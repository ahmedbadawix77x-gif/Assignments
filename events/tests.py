from django.test import TestCase, Client
import json
from .models import Event


class EventAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_crud_cycle(self):
        # 1. Create Event
        payload = {
            "name": "Magic Party",
            "description": "Fun times at the castle",
            "location": "Hogwarts",
            "start_date": "2025-01-01T10:00:00Z",
            "end_date": "2025-01-01T12:00:00Z"
        }
        response = self.client.post(
            "/events/create/", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        event_id = response.json()["id"]

        # 2. Get All Events
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # 3. Get Single Event
        response = self.client.get(f"/events/{event_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Magic Party")

        # 4. Update Event (PATCH)
        patch_payload = {"location": "Diagon Alley"}
        response = self.client.patch(
            f"/events/{event_id}/update/", data=json.dumps(patch_payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)

        # Verify update
        response = self.client.get(f"/events/{event_id}/")
        self.assertEqual(response.json()["location"], "Diagon Alley")

        # 5. Delete Event
        response = self.client.delete(f"/events/{event_id}/delete/")
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        response = self.client.get(f"/events/{event_id}/")
        self.assertEqual(response.status_code, 404)
