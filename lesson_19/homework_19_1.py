import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"


response = requests.get(search_url, search_params)
json_obj = response.json()
# dict_keys(['version', 'href', 'items', 'metadata', 'links'])

list_of_nasa_ids = []
for obj in json_obj.get('collection').get('items')[:2]:
    list_of_nasa_ids.append(obj.get('data')[0].get('nasa_id'))
# print(list_of_nasa_ids)

for idx, nasa_id in enumerate(list_of_nasa_ids):
    urls_response = requests.get(asset_url_template.format(nasa_id=nasa_id))
    urls_json = urls_response.json()
    for item in urls_json.get('collection').get('items'):
        img_url = item.get('href')
        if img_url.endswith('.jpg'):
            img_data = requests.get(img_url).content
            with open(f"mars_photo{idx+1}.jpg", "wb") as f:
                f.write(img_data)
            break

