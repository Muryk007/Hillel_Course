import requests
import logging

logger = logging.getLogger("nasa")

class NasaController:
    def __init__(self,
                 url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos/'
                 ):
        self.url = url

    def get_photos(self, sol, camera, api_key):
        params = {
            'api_key': api_key,
            'sol': sol,
            'camera': camera,
        }
        response = requests.get(self.url, params=params)
        logger.info(f"get_photos response: {response}")
        return response

