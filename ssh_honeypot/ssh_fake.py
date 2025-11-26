import socket
from datetime import datetime
import os

# Config
HOST = "0.0.0.0"
PORT = 2223  # non-standard SSH port to avoid conflict
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "connections.log")

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_attempt(addr, username, password):
    with open(LOG_FILE, "a") as f:
        f.write(f"{get_timestamp()} - {addr[0]}:{addr[1]} - Username: {username}, Password: {password}\n")

def start_ssh_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] SSH honeypot listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[!] Connection from {addr}")
                conn.sendall(b"SSH-2.0-OpenSSH_7.9p1 Ubuntu-10\n")
                try:
                    # Fake prompt
                    conn.sendall(b"login: ")
                    username = conn.recv(1024).decode(errors='ignore').strip()
                    conn.sendall(b"password: ")
                    password = conn.recv(1024).decode(errors='ignore').strip()
                    log_attempt(addr, username, password)
                    conn.sendall(b"Permission denied, please try again.\n")
                except Exception as e:
                    log_attempt(addr, "Error", str(e))

if __name__ == "__main__":
    start_ssh_honeypot()
