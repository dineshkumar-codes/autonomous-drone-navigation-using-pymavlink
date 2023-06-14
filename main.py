from pymavlink import mavutil
import time

takeoff_alt = int(input("takeoff_alt: "))
target_alt = int(input("wp_alt: "))
target_lat = float(input("latitude: "))
target_long = float(input("longitude: "))

# Start a connection listening to a UDP port
drone = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat
# This sets the system and component ID of remote system for the link
drone.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (drone.target_system, drone.target_component))

# Send a command to set the drone's mode to "Guided"
print("Setting guided mode...")
drone.set_mode('GUIDED', 0)    

# Arming the drone
print("Arming the drone")
drone.mav.command_long_send(drone.target_system, drone.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
msg = drone.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)

# Take-off the drone
print("Taking off")
drone.mav.command_long_send(drone.target_system, drone.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, takeoff_alt)

# Monitor altitude
while True:
      msg = drone.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
      if abs(msg.relative_alt/1000 - takeoff_alt) <= 1:
        print(f"Set take-off altitude {takeoff_alt} meters reached!")
        break
      time.sleep(0.1)

# Send drone to given coordinate
drone.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, drone.target_system,
                        drone.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, int(0b110111111000), int(target_lat * 10 ** 7), int(target_long * 10 ** 7), target_alt, 0, 0, 0, 0, 0, 0, 0 , 0))

