import pytest
from app import app as APIAppRoot
from fastapi.testclient import TestClient


@pytest.fixture(scope="package")
def client():
    with TestClient(APIAppRoot, base_url="http://testserver/api/netease/") as client:
        yield client


def test_search(client: TestClient):
    response = client.get("search", params={"s": "test"})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_artist(client: TestClient):
    response = client.get("artist", params={"id": 1024317})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_album(client: TestClient):
    response = client.get("album", params={"id": 63263})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_detail(client: TestClient):
    response = client.get("detail", params={"id": 657666})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_song(client: TestClient):
    response = client.get("song", params={"id": 657666})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_playlist(client: TestClient):
    response = client.get("playlist", params={"id": 39983375})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_lyric(client: TestClient):
    response = client.get("lyric", params={"id": 657666})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_mv(client: TestClient):
    response = client.get("mv", params={"id": 425588})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_comments(client: TestClient):
    response = client.get("comments", params={"id": 657666})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_record(client: TestClient):
    response = client.get("record", params={"id": 286609438})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_djradio(client: TestClient):
    response = client.get("djradio", params={"id": 350596191})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_dj(client: TestClient):
    response = client.get("dj", params={"id": 10785929})
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_detail_dj(client: TestClient):
    response = client.get("detail_dj", params={"id": 1370045285})
    assert response.status_code == 200
    assert response.json()["code"] == 200
