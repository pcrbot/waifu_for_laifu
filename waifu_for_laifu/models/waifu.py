import base64
from io import BytesIO

from PIL import Image


class Waifu:

    def __init__(self, new_girl):
        self.image_data = base64.b64decode(new_girl['image'])
        self.seeds = new_girl['seeds']

    def get_image(self):
        return Image.open(BytesIO(self.image_data))
