from encrypt_decrypt import generate_key, encrypt_message
from face_authenticate import authenticate_face
import socket

generate_key()

if authenticate_face():
    msg = input("Enter message to send securely: ")
    encrypted_msg = encrypt_message(msg)

    s = socket.socket()
    s.connect(("localhost", 12345))
    s.send(encrypted_msg)
    print("[INFO] Encrypted message sent.")
    s.close()
else:
    print("[ERROR] Face not authenticated.")
