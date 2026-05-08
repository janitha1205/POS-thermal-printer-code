import serial
import time

# 1. Configuration
# GOOJPRT PT-210 usually uses 9600 baud for Bluetooth/Serial
PORT = 'COM6' 
BAUD = 115200

try:
    # 2. Open the connection
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        print(f"Connected to {PORT}")

        # 3. ESC/POS Commands (Standard Control Codes)
        # Initialize printer (ESC @)
        ser.write(b'\x1b\x40') 
        
        # 4. Sending Text
        ser.write(b"GOOJPRT PT-210 Test\n")
        ser.write(b"--------------------------\n")
        
        # Formatting Example: Bold On (ESC E 1)
        ser.write(b'\x1b\x45\x01')
        ser.write(b"Done by janitha thalagoda!\n")
        ser.write(b'\x1b\x45\x00') # Bold Off
        
        # 5. Paper Feed
        # Feed 3 lines so you can tear the paper
        ser.write(b"\n\n\n")
        
        print("Print job sent!")

except serial.SerialException as e:
    print(f"Could not open {PORT}. Is it already in use or paired? Error: {e}")
