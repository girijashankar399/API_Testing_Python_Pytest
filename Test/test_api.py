import requests
import pytest
# from config.config import BASE_URL
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"

def test_update_post():
    payload = {"title": "updated title"}
    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

