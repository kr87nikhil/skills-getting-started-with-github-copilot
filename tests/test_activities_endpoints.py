"""Tests for the GET /activities endpoint."""

import pytest


def test_get_activities_success(client):
    """Test that GET /activities returns all activities successfully."""
    response = client.get("/activities")
    
    assert response.status_code == 200
    activities = response.json()
    
    # Should return the three sample activities
    assert len(activities) == 3
    assert "Chess Club" in activities
    assert "Programming Class" in activities
    assert "Debate Club" in activities


def test_get_activities_structure(client):
    """Test that GET /activities response has the expected structure."""
    response = client.get("/activities")
    
    assert response.status_code == 200
    activities = response.json()
    
    # Verify each activity has required fields
    for activity_name, activity_data in activities.items():
        assert isinstance(activity_data, dict)
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)
