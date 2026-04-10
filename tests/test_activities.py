import urllib.parse

def test_get_activities(client):
    # Arrange/Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data

def test_signup_success_adds_participant(client):
    # Arrange
    activity = "Basketball Club"
    email = "tester@example.com"
    # Act
    url = f"/activities/{urllib.parse.quote(activity)}/signup?email={urllib.parse.quote(email)}"
    resp = client.post(url)
    # Assert
    assert resp.status_code == 200
    get = client.get("/activities")
    assert email in get.json()[activity]["participants"]

def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"
    url = f"/activities/{urllib.parse.quote(activity)}/signup?email={urllib.parse.quote(existing)}"
    # Act
    resp = client.post(url)
    # Assert
    assert resp.status_code == 400

def test_signup_nonexistent_returns_404(client):
    # Arrange
    activity = "NoSuchActivity"
    email = "nobody@example.com"
    url = f"/activities/{urllib.parse.quote(activity)}/signup?email={urllib.parse.quote(email)}"
    # Act
    resp = client.post(url)
    # Assert
    assert resp.status_code == 404
