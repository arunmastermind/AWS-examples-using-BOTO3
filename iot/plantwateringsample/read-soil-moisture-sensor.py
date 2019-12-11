import RPi.GPIO as GPIO
import time

# Represents the GPIO21 pin. 
channel = 21

# Use the GPIO BCM pin numbering scheme.
GPIO.setmode(GPIO.BCM)

# Receive input signals through the pin.
GPIO.setup(channel, GPIO.IN)

# Infinite loop to keep this script running.
while True:
  # 'No water' = 1/True (sensor's microcontroller light is off).
  if GPIO.input(channel):
    print("No water detected")
  else:
    # 'Water' = 0/False (microcontroller light is on).
    print("Water detected!")

  # Wait 5 seconds before checking again.
  time.sleep(5)

# Clean things up if for any reason we get to this
# point before script stops.
GPIO.cleanup()