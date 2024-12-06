import tkinter as tk
from tkinter import messagebox
import requests
import random

# OpenWeather API key
API_KEY = "66c70088cfcec844eff04e5bd11f22f7"


# Function to fetch weather data
def fetch_weather():
    global city  # Save city for dynamic updates
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    # OpenWeather API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            # Display weather data
            weather_label.config(text=f"Weather: {weather}")
            temp_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")

            # Updating of sensor values
            update_sensors()
        else:
            messagebox.showerror("Error", f"City not found. HTTP {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Simulate and update sensor data every 5 seconds
def update_sensors():
    # Simulate accelerometer data
    accel_x = random.uniform(-10, 10)
    accel_y = random.uniform(-10, 10)
    accel_z = random.uniform(-10, 10)

    # Simulate magnetometer data
    magnet_x = random.uniform(-50, 50)
    magnet_y = random.uniform(-50, 50)
    magnet_z = random.uniform(-50, 50)

    # Updating labels with new data
    accel_label.config(text=f"Accelerometer: X={accel_x:.2f}, Y={accel_y:.2f}, Z={accel_z:.2f}")
    magnet_label.config(text=f"Magnetometer: X={magnet_x:.2f}, Y={magnet_y:.2f}, Z={magnet_z:.2f}")

    # Schedule the function to run again after 5 seconds
    root.after(5000, update_sensors)


root = tk.Tk()
root.title("WeatherSense - Real-Time Data Visualization")
root.geometry("400x400")

city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Weather & Sensors", font=("Arial", 12), command=fetch_weather)
fetch_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12))
weather_label.pack(pady=5)
temp_label = tk.Label(root, text="", font=("Arial", 12))
temp_label.pack(pady=5)
humidity_label = tk.Label(root, text="", font=("Arial", 12))
humidity_label.pack(pady=5)

accel_label = tk.Label(root, text="", font=("Arial", 12))
accel_label.pack(pady=10)
magnet_label = tk.Label(root, text="", font=("Arial", 12))
magnet_label.pack(pady=10)

root.mainloop()
