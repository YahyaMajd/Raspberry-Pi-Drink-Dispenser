# Import necessary packages
from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import requests
import serial
import json
import time

# Create a Flask app instance
app = Flask(__name__)

# Enable cross-origin resource sharing for the app
CORS(app)

# Initialize the serial port connection
ser = None
try:
    ser = serial.Serial('/dev/cu.usbmodem14601', baudrate=9600, timeout = 3)
    time.sleep(2)
except Exception as e:
    print(f"Failed to initialize serial port: {str(e)}")
    

# Define a Flask route for dispensing drinks
@app.route('/', methods=['POST'])
def process_dispense_request():
    # Extract the JSON data from the request
    data = request.get_json() 
    # Initialize the drink variable
    drink = None
    # Check which drink was requested and send the corresponding command to the serial device
    if data and 'TEQUILA_SUNRISE' in data:
        print("Processing dispense request...")
        drink = 'Tequila Sunrise'
        sendData("TEQUILA_SUNRISE")
    elif data and 'GIN_TONIC' in data:
        drink = 'Gin and Tonic'
        sendData("GIN_TONIC")
    elif data and 'MANGO_RUM' in data:
        drink = 'Mango Rum Fizz'
        sendData("MANGO_RUM")
    elif data and 'RUM_COKE' in data:
        drink = 'Rum and Coke '
        sendData("RUM_COKE")
    elif data and 'ORANGE_VODKA' in data:
        drink = 'Orange Vodka'
        sendData("ORANGE_VODKA")

    # Return a JSON response indicating success and which drink was dispensed
    return make_response(jsonify({'success': True, 'drink': drink}))

# Helper function to send data to the serial device
def sendData(data):
    # Check if the serial port was initialized
    if ser is None:
        print("Serial port not initialized")
        return
    try:
        # Print a message indicating that data is being sent
        print(f"Sending data: {data}")
        # Send the data to the serial device
        ser.write(bytes(data + '\n','UTF-8'))
        # Print a message indicating that data was sent successfully
        print("Data sent successfully")
    except Exception as e:
        # Print an error message if data could not be sent to the serial device
        print(f"Failed to send data: {str(e)}")

# Run the Flask app with debugging enabled and listen on all available network interfaces
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
