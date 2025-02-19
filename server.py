import socket
from utils.crypto_utils import CryptoUtils
from utils.image_utils import ImageUtils

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("Server started...")

    while True:
        data, addr = server_socket.recvfrom(65536)
        print(f"Received data from {addr}")

        # Decrypt the image
        key = b'your-secure-key-32-bytes-long'
        decrypted_data = CryptoUtils.decrypt_aes(key, data)
        image = ImageUtils.bytes_to_image(decrypted_data)

        # Save the image
        ImageUtils.save_image(image, 'received_image.png')
        print("Image saved as received_image.png")

if __name__ == "__main__":
    start_server()
