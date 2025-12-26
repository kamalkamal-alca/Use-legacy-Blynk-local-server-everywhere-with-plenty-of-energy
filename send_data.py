import BlynkLib
from BlynkTimer import BlynkTimer
import Adafruit_DHT
import time
import sys

# Blynk authentication token
BLYNK_AUTH_TOKEN = 'CNWvcPHw3oVf1kgRJpHZwxINO4W66ICI'

# Initialize Blynk - added connection timeout and error handling
try:
    blynk = BlynkLib.Blynk(
        BLYNK_AUTH_TOKEN,
        server="192.168.2.101",
        port=8080
    )
    print("Blynk initialized successfully")
except Exception as e:
    print(f"Error initializing Blynk: {e}")
    sys.exit(1)

# Initialize timer
timer = BlynkTimer()

# DHT11 sensor setup
SENSOR_TYPE = Adafruit_DHT.DHT11  # Changed to use constant
SENSOR_PIN = 27

def read_tempC():
    try:
        # Read from DHT11 sensor
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
        
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.1f}*C, Humidity: {humidity:.1f}%")
            
            # Send data to Blynk virtual pins
            blynk.virtual_write(9, temperature)
            blynk.virtual_write(10, humidity)
        else:
            print("Failed to retrieve data from sensor")
            
    except Exception as e:
        print(f"Error reading sensor: {e}")

# Set up the timer to read sensor every 2 seconds
timer.set_interval(2, read_tempC)

# Main loop
try:
    print("Starting main loop...")
    while True:
        blynk.run()
        timer.run()
        time.sleep(0.1)  # Small delay to prevent CPU overuse
        
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    sys.exit(0)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
