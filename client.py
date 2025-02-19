import socket
from utils.crypto_utils import CryptoUtils
from utils.image_utils import ImageUtils

def send_image(image_path):
    # Load the image
    image = ImageUtils.load_image(image_path)
    image_bytes = ImageUtils.image_to_bytes(image)

    # Encrypt the image
    key = b'your-secure-key-32-bytes-long'
    encrypted_data = CryptoUtils.encrypt_aes(key, image_bytes)

    # Send the encrypted data
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(encrypted_data, ('localhost', 12345))
    print("Image sent successfully")

if __name__ == "__main__":
    send_image('input_image.png')
