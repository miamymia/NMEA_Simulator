import time
import socket


HOST = '127.0.0.1'
PORT = 65432

# Create TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            # TCP(IP)
            nmea = client.recv(1024)
            time.sleep(10)
            if not nmea:
                print(f"No more data from {HOST}:{PORT}")
                break
            print(f"Received data from {nmea.decode('utf-8').strip()}")
            response = nmea.decode('utf-8').strip()
            client.sendall(response.encode('utf-8'))
            print(f"Sent {response} to server")
    except Exception as e:
        print(f"Error connecting to server: {e}")


