from homework_19_2 import ImageClient
import pytest
import os

@pytest.fixture
def api_client():
    return ImageClient("http://127.0.0.1:8080")

@pytest.fixture
def image_path():
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'mars_photo1.jpg')


@pytest.fixture
def uploaded_filename(api_client, image_path):
    resp = api_client.upload_image(image_path)
    filename = resp.json()['image_url'].split('/')[-1]

    yield filename
    api_client.delete_image(filename)

class TestImageAPI:
    def test_post_image(self, api_client, image_path):
        response = api_client.upload_image(image_path)
        assert response.status_code == 201
        assert "image_url" in response.json()

    def test_get_image_info(self, api_client, uploaded_filename):
        response = api_client.get_image_info(uploaded_filename)
        assert response.status_code == 200
        assert uploaded_filename in response.json()['image_url']

    def test_delete_image(self, api_client, uploaded_filename):
        response = api_client.delete_image(uploaded_filename)
        assert response.status_code == 200
        assert "deleted" in response.json()['message']
