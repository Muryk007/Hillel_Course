# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi.
# Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg, mars_photo2.jpg.
# Завдання потрiбно зробити використовуючи модуль requests

import requests
import pathlib

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

photos_dir = pathlib.Path(__file__).parent / "NASA_Mars_Photos"
photos_dir.mkdir(exist_ok=True)

response = requests.get(url=url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos',[])

    for i, photo in enumerate(photos, start=1):
        img_url = photo["img_src"]

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            file_path = photos_dir / f"mars_photo{i}.jpg"
            with open(file_path, "wb") as f:
                f.write(img_response.content)

    print(f"Downloaded {len(photos)} photos")

