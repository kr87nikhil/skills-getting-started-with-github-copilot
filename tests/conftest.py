"""Pytest configuration and shared fixtures for backend tests."""

import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def sample_activities():
    """Fixture providing sample activity data for tests."""
    return {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu"]
        },
        "Debate Club": {
            "description": "Develop critical thinking and public speaking skills through competitive debates",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": []
        }
    }


@pytest.fixture
def client(monkeypatch, sample_activities):
    """Fixture providing a TestClient with mocked activities data."""
    # Replace the activities dict in the app with sample data for test isolation
    monkeypatch.setattr("src.app.activities", sample_activities)
    return TestClient(app)
