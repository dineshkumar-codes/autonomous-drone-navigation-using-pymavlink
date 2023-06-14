# autonomous-drone-navigation-using-pymavlink
This repository contains a Python script that demonstrates drone control using MAVLink protocol. The script connects to a drone using a UDP port and performs various actions such as takeoff and waypoint navigation.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed
- `pymavlink` library installed (use `pip install pymavlink` to install)

## Usage

1. Open the terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
  `python ./main.py`
4. You will be prompted to enter the takeoff altitude, waypoint altitude, latitude, and longitude.
5. The script will establish a connection with the drone and set it to guided mode.
6. It will arm the drone and initiate takeoff to the specified altitude.
7. Once the takeoff altitude is reached, the script will send the drone to the given coordinate.
8. Monitor the console output for updates on the script's progress.

Note: Make sure to adjust the UDP port (14551) in the code if necessary to match your specific setup.

![Autonomous drone navigation using pymavlink](https://youtu.be/hEtf-eoJXkU)
