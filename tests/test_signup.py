"""Tests for the POST /activities/{activity_name}/signup endpoint."""

import pytest


def test_signup_success(client):
    """Test that a student can successfully sign up for an activity."""
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Signed up {email} for {activity_name}"
    
    # Verify the student was added to participants
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email in activities[activity_name]["participants"]


def test_signup_already_registered(client):
    """Test that signing up twice returns a 400 error."""
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already registered in sample data
    
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"].lower()


def test_signup_activity_not_found(client):
    """Test that signing up for a non-existent activity returns 404."""
    activity_name = "Non-Existent Activity"
    email = "student@mergington.edu"
    
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()
