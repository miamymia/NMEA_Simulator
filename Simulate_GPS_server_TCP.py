import time
import socket
import argparse

"""
Script to simulate live vessel position information.
read an example nmea file and send it line-by-line via TCP connection on local host
To use e.g. with PosiView, see screenshots for configuration. Set the same port in Posiview as set below
Also usable with client script (e.g. Simulate_GPS_client_TCP.py)
Usage: python Simulate_GPS_server_TCP.py path/to/example_nmea.txt

Author: Mia Schumacher/GEOMAR
Date: 08/2025 v1.0
"""


def simulate_nmea(nmea_file):
    HOST = '127.0.0.1'
    PORT = 65432

    # Create TCP/IP socket/ Create UDP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # allow reuse of address
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server listening on port {HOST}:{PORT}")

        #TCP(IP)
        conn, addr = server.accept()

        with conn:
           print(f"Connected to {addr}.")
           #nmea_file = args     
           try:
                with open(nmea_file, 'r') as nmea:
                    while True:
                        for line in nmea:
                            print(line.strip())
                            # for TCP/IP:
                            conn.sendall(line.encode('utf-8'))
                            print(f"Sent {line.strip()}")
                            time.sleep(1)
           except Exception as e:
               print(f"Error reading {nmea_file}. Exception thrown {e}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to simulate live position data sent over network')
    parser.add_argument("filepath", metavar="FILE", help="Path to nmea file")
    args = parser.parse_args()
    simulate_nmea(args.filepath)

        


