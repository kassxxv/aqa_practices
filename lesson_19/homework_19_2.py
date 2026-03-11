import requests
import os

class ImageClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload_image(self, file_path):
        url = f"{self.base_url}/upload"
        filename = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            response = requests.post(url, files={'image': (filename, f, 'image/jpeg')})
        return response

    def get_image_info(self, filename):
        url = f"{self.base_url}/image/{filename}"
        response = requests.get(url, headers={'Content-Type': 'text'})
        return response

    def delete_image(self, filename):
        url = f"{self.base_url}/delete/{filename}"
        response = requests.delete(url)
        return response
