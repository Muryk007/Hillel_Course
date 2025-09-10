import pytest
import sys
import pathlib
import logging.config

project_root = pathlib.Path(__file__).parent.parent  # /Hillel_Project
sys.path.insert(0, str(project_root))

from core.api_tests.nasa.nasa_controller import NasaController
from lesson_19_1.homework_19_1 import nasa_photos



log_file = pathlib.Path(__file__).parent / "nasa_muratov.log"

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
)

logger = logging.getLogger('nasa')

@pytest.mark.nasa
@pytest.mark.parametrize ("sol, camera, api_key",[(1000, 'fhaz', 'b0r8xbdoqU55nQncQO4swlMYhQaWdgRBSwrbgtCj')])
def test_get_nasa_photos(sol, camera, api_key):
    response = NasaController().get_photos(sol, camera, api_key)
    if response.status_code != 200:
        logger.error(f"Помилка! {response.status_code} {response.text}")
        return
    assert response.status_code == 200


    data = response.json()
    assert "photos" in data
    assert isinstance(data["photos"], list)

# def test_get_nasa_photos_error():
#      response = NasaController().get_photos(1000, 'fhaz', 'b0r8xbdoqU55nQncQO4swlMYhQaWdgRBSwrbgtCj')
#      assert response.status_code == 403


def test_save_nasa_photos():

    photos_dir = nasa_photos(sol=1000, camera="fhaz", api_key="b0r8xbdoqU55nQncQO4swlMYhQaWdgRBSwrbgtCj")

    if not photos_dir.is_dir():
        logger.error(f"{photos_dir} не існує")
    assert photos_dir.is_dir(), f"{photos_dir} не існує"

    files = list(photos_dir.iterdir())
    if not files:
        logger.error(f"{photos_dir} порожня")
    assert files, f"{photos_dir} порожня"

    # Перевіряємо, що всі файли - картинки
    valid_extensions = (".jpg", ".jpeg", ".png")
    for f in files:
        if f.suffix.lower() not in valid_extensions:
            logger.error(f"{f.name} не є картинкою")
        assert f.suffix.lower() in valid_extensions, f"{f.name} не є картинкою"


