import tkinter as tk
import requests

HEIGHT = 600
WIDTH = 600


def test_function(entry):
    print("The entry is :", entry)

def get_weather(city):
    Weather_key = '6afb91ffe7174e789a1ed0a1b7b58095'
    url = 'http://api.openweathermap.org/data/2.5/forecast?'
    params = {'appid ': Weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    print(response.json())

root = tk.Tk()
title = root.title("Weather Software")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_image = background_image.zoom(3)
background_label = tk.Label(root, image=background_image)
background_label.place(anchor='n',relx=0.5, rely=0, relwidth=0.999, relheight=1)

header = tk.Label(root, text="Weather App", bg='white', font=40)
header.place(relx=0.521, rely=0.95, relwidth=0.3, relheight=0.05, anchor='s')

frame = tk.Frame(root, bg='#19a2fc', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.09, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx=0.01, rely=0.1, relwidth=0.78, relheight=0.9)
 
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.8, rely=0.1, relwidth=0.19, relheight=0.9)

lower_frame = tk.Frame(root, bg='#19a2fc', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white')
label.place(relwidth=1, relheight=1)

root.mainloop()

