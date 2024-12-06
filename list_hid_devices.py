import pywinusb.hid as hid

# Function to list HID devices and check for accelerometers
def list_hid_devices():
    all_devices = hid.HidDeviceFilter().get_devices()
    accelerometer_device = None
    for device in all_devices:
        print("Device found:", device.product_name)
        # Check if device name contains 'accelerometer' (customize this for your device)
        if "accelerometer" in device.product_name.lower():
            accelerometer_device = device
            print("Accelerometer found:", device.product_name)
    return accelerometer_device

# Running the function
accelerometer = list_hid_devices()
if accelerometer:
    print("Accelerometer Device Found")
else:
    print("No Accelerometer found")
