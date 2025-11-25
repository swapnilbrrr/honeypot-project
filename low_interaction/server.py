import socket
from datetime import datetime
import os

# Log directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "connections.log")

# Fake service configuration
HOST = "0.0.0.0"     # Listen on all interfaces
PORT = 2222          # Honeypot port

def get_timestamp():
    """Return SOC-style timestamp without microseconds."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_connection(addr, data):
    """Append attacker activity to the log file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{get_timestamp()} - {addr[0]}:{addr[1]} - {data}\n")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Low-interaction honeypot listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[!] Connection from {addr}")

                conn.sendall(b"Welcome to the fake service!\n")

                try:
                    # Continuously read attacker input
                    while True:
                        data = conn.recv(1024).decode(errors='ignore').strip()

                        if not data:
                            log_connection(addr, "Attacker disconnected")
                            break

                        log_connection(addr, data)

                except Exception as e:
                    log_connection(addr, f"Error reading data: {e}")

if __name__ == "__main__":
    start_server()
