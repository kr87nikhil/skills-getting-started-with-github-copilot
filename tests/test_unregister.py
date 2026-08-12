"""Tests for the DELETE /activities/{activity_name}/unregister endpoint."""

import pytest


def test_unregister_success(client):
    """Test that a student can successfully unregister from an activity."""
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already registered in sample data
    
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Unregistered {email} from {activity_name}"
    
    # Verify the student was removed from participants
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email not in activities[activity_name]["participants"]


def test_unregister_not_registered(client):
    """Test that unregistering a non-registered student returns 400."""
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"
    
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    assert response.status_code == 400
    data = response.json()
    assert "not registered" in data["detail"].lower()


def test_unregister_activity_not_found(client):
    """Test that unregistering from a non-existent activity returns 404."""
    activity_name = "Non-Existent Activity"
    email = "student@mergington.edu"
    
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()
