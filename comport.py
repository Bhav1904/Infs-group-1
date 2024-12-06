import serial

# Set your COM port (you should find this after running the list_hid_devices.py)
# Example COM port: 'COM3'. Update it to the correct port for your device.
com_port = 'COM3'

# Function to read accelerometer data from the serial port
def read_accelerometer_data():
    try:
        # Connect to the USB accelerometer (adjust port and baudrate as needed)
        ser = serial.Serial(com_port, 9600)  # Adjust the port and baudrate to match your device
        # Read data continuously from the accelerometer
        data = ser.readline().decode('utf-8').strip()  # Decode data from the serial port
        return data
    except Exception as e:
        print("Error:", e)
        return None

# For testing purpose, you can call this function here:
if __name__ == "__main__":
    while True:
        data = read_accelerometer_data()
        if data:
            print("Accelerometer Data:", data)
        else:
            print("No data from accelerometer")
