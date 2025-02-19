import cv2
import numpy as np
from PIL import Image

class ImageUtils:
    @staticmethod
    def load_image(image_path):
        return cv2.imread(image_path)

    @staticmethod
    def save_image(image, output_path):
        cv2.imwrite(output_path, image)

    @staticmethod
    def image_to_bytes(image):
        return cv2.imencode('.png', image)[1].tobytes()

    @staticmethod
    def bytes_to_image(image_bytes):
        return cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    @staticmethod
    def resize_image(image, width, height):
        return cv2.resize(image, (width, height))
