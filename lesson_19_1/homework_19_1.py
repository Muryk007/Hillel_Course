# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi.
# Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg, mars_photo2.jpg.
# Завдання потрiбно зробити використовуючи модуль requests

import requests
import pathlib
import logging

logger = logging.getLogger('nasa')

def nasa_photos(sol=1000, camera='fhaz', api_key='DEMO_KEY'):
    photos_dir = pathlib.Path(__file__).parent / "NASA_Mars_Photos"
    photos_dir.mkdir(exist_ok=True)

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': sol, 'camera': camera, 'api_key': api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Помилка при зверненні до АРІ {e}")
        return photos_dir

    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        logger.info(f"Фото для sol={sol} та camera={camera} відсутні")
        return photos_dir

    for i, photo in enumerate(photos, start=1):
        img_url = photo["img_src"]
        if not img_url:
            continue
        try:
            img_response = requests.get(img_url)
            logger.info(f"Завантажую {img_url}")
            img_response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Не вдалося завантажити {img_url}: {e}")
            continue

        file_path = photos_dir / f"mars_photo{i}.jpg"
        with open(file_path, "wb") as f:
            f.write(img_response.content)

    logger.info(f"Збережено {len(list(photos_dir.iterdir()))} фото у {photos_dir}")
    return photos_dir