import requests

API_BASE_URL = "http://localhost:5000"

def test_get_episodes():
    """Test fetching all episodes without filters."""
    response = requests.get(f"{API_BASE_URL}/episodes")
    assert response.status_code == 200
    assert isinstance(response.json(), list), "Response should be a list of episodes"

def test_get_episodes_by_month():
    """Test fetching episodes filtered by month."""
    response = requests.get(f"{API_BASE_URL}/episodes", params={"month": "1"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_episodes_by_subject():
    """Test fetching episodes filtered by subject."""
    response = requests.get(f"{API_BASE_URL}/episodes/subject", params={"subject": "Mountain"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_episodes_by_color():
    """Test fetching episodes filtered by color."""
    response = requests.get(f"{API_BASE_URL}/episodes/color", params={"color": "Phthalo Blue"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

if __name__ == "__main__":
    test_get_episodes()
    test_get_episodes_by_month()
    test_get_episodes_by_subject()
    test_get_episodes_by_color()

    print("All tests passed!")
