import requests as req
import tkinter as tk
from tkinter import messagebox

def get_weather(input_city):
    api_key = "5dfac86ff36fdc0a5506a69ae0fbe7f4"
    city = input_city
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    completURL = f"{base_url}&appid={api_key}&q={city}&units=metric"

    response = req.get(completURL)
    data = response.json()

    if data['cod'] != '404':
        main = data['main']
        weather_desk = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']

        suggestion = ''

        if temp < 10:
            suggestion = "بهتر است لباس گرم بپوشی مثل کاپشن"
        elif 10 <= temp >= 20:
            suggestion = "ژاکت یا پلیور کافی است"
        else:
            suggestion = "بهتر است لباس نازک بپوشی"

        weather_info = f"city:  {city}\ntemp:  {temp}\ndescription:  {weather_desk}\nhumidity:  {humidity}\nپیشنهاد: {suggestion}"

    else:
        weather_info = "شهری یافت نشد"

    return weather_info

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        messagebox.showinfo("اطلاعات هواشناسی", weather_info)
    else:
        messagebox.showwarning("هشدار", "لطفاً نام شهر را وارد کنید!")

app = tk.Tk()
app.title("برنامه هواشناسی")
app.geometry("400x400")

city_lable = tk.Label(app, text="نام شهر:", width=20, height=2)
city_lable.pack(pady=20)

city_entry = tk.Entry(app)
city_entry.pack(pady=20)

weather_button = tk.Button(app, text="نمایش وضعیت هوا", command=show_weather)
weather_button.pack(pady=20)

app.mainloop()
