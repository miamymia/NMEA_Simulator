# NMEA_Simulator
**Simulates live position data in nmea format sent over local network**

`Simulate_GPS_server_TCP.py` reads an example nmea file (e.g. `output.nmea`) and send it line-by-line via TCP connection on local host
To use e.g. with PosiView (QGIS plugin), see screenshots for configuration. Set the same port in Posiview as set in `Simulate_GPS_server_TCP.py`.

**General Usage**: `python Simulate_GPS_server_TCP.py path/to/example_nmea.txt`

It is also usable with a client script (e.g. `Simulate_GPS_client_TCP.py`). Start the server script first and then run client in another shell.