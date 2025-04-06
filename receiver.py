from encrypt_decrypt import decrypt_message
import socket

s = socket.socket()
s.bind(("localhost", 12345))
s.listen(1)

print("[INFO] Waiting for incoming message...")
conn, addr = s.accept()

data = conn.recv(1024)
decrypted_msg = decrypt_message(data)

print("[SUCCESS] Decrypted Message Received:")
print("➡️", decrypted_msg)

conn.close()
