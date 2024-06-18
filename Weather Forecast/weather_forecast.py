import requests
import tkinter as tk

def get_weather():
    api_key = "7a790157fdc0f0770cb4dfd11af5f843"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city_name = entry_location.get()
    complete_url = f"{base_url}?q={city_name}&appid={api_key}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        temperature_label = tk.Label(frame_result, text=f"Temperature: {data['main']['temp']} C")
        humidity_label = tk.Label(frame_result, text=f"Humidity: {data['main']['humidity']}%")
        wind_speed_label = tk.Label(frame_result, text=f"Wind Speed: {data['wind']['speed']} m/s")
        pressure_label = tk.Label(frame_result, text=f"Pressure: {data['main']['pressure']} hPa")
        # I can't find the precipitation in the data

        temperature_label.grid(row=0, column=0, sticky="w", pady=2)
        humidity_label.grid(row=1, column=0, sticky="w", pady=2)
        wind_speed_label.grid(row=2, column=0, sticky="w", pady=2)
        pressure_label.grid(row=3, column=0, sticky="w", pady=2)
    else:
        error_label = tk.Label(frame_result, text=f"Error: {response.status_code}")
        error_label.grid(row=0, column=0, sticky="w", pady=2)

window = tk.Tk()
window.title("Weather Forecast")
window.minsize(width=600, height=400)

frame_location = tk.Frame(window)
frame_location.pack(pady=10)

label_location = tk.Label(master=frame_location, text="Location:")
label_location.pack(side=tk.LEFT, padx=5)
entry_location = tk.Entry(master=frame_location)
entry_location.pack(side=tk.LEFT, padx=5)
button = tk.Button(frame_location, text="Get Weather", command=get_weather)
button.pack(side=tk.LEFT, padx=10)

frame_result = tk.Frame(window)
frame_result.pack(pady=20)

window.mainloop()
