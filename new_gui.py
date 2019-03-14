from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import folium
from tkinter import messagebox
from tkinter import ttk
import os
import webbrowser
from info_parser import Info


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


import tkinter as tk
root = tk.Tk()
root.title('Weather')
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# background
back_photo = ImageTk.PhotoImage(Image.open('wwww.jpg'))
w = Label(root, image=back_photo)
w.pack()
# Application Logo
app_name = ImageTk.PhotoImage(Image.open('appname.png'))
w = Label(root, image=app_name, bg=_from_rgb((73,183,232)))
w.place(x=x/3, y=20)
#City Country entry
city_names = StringVar()
entry_1 = ttk.Entry(root,textvariable=city_names)
city_names.set("Enter City Here ...")
entry_1.place(x=x-300, y=30)
#Personal Info with Button
def helo():
    new_root = Tk()
    new_root.title('Personal Info')

    new_root.resizable(width=False, height=False)
    new_root.geometry('250x300')
    parse = Info().get_personal_info()
    x_axis = 10
    y_axis = 10
    for k, v in parse.items():
        key_label = Label(new_root, text=f'{k}: -- {v}', fg='blue').place(x=x_axis, y=y_axis)

        value_label = None
        y_axis += 20

    root.mainloop()

dijkstra = Button(root, command=helo)
personal_info = ImageTk.PhotoImage(Image.open('personal_info.png'))
dijkstra.config(image=personal_info,  bg=_from_rgb((73,183,232)))
dijkstra.place(x=100, y=100)

# Seach Button

a = Button(root)
search = ImageTk.PhotoImage(Image.open('research.png'))
a.config(image=search)
a.place(x=x-170, y=28.5)

# CheckButtons

def get_cel():
    temprature_label.configure(text='{} Celsius'.format(temprature))

def get_kelvin():
    temprature_label.configure(text='{} Kelvin'.format(temprature+273.15))

def get_fare():
    temprature_label.configure(text='{} Farenheit'.format(temprature * 9/5 +32))
check_bt_cel = ttk.Checkbutton(root, text='Celsius', command=get_cel)

check_bt_cel.place(x=x-297, y=70)
check_bt_kel = ttk.Checkbutton(root, text='Kelvin', command=get_kelvin)
check_bt_kel.place(x=x-297, y=90)
check_bt_fh = ttk.Checkbutton(root, text='Farenheit', command=get_fare)
check_bt_fh.place(x=x-297, y=110)

#Default window
def make_default_window():
    obj = Info()
    obj.get_personal_info()
    url_base = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    APIKEY = '3fcb9950908ddd9b5672e2a29e4842a2'
    city_name = obj.city
    country_name = obj.country
    global city_country_lable
    global temprature_label
    global lat_long_label
    city_country_lable = Label(root, text=f'{city_name}, {country_name}', font='Verdana 32 bold italic', bg=_from_rgb((73,183,232)), fg='white').place(x=x/2.75, y=130)
    req = requests.get(url_base.format(city_name, APIKEY))
    default_x = req.json()
    global temprature
    temprature = None
    pressure = None
    global lat
    global long
    lat, long = None, None
    description = None
    for j in default_x:
        main = default_x['main']
        if temprature is None:
            temprature = round(main['temp'] -273.15, 2)
        if pressure is None:
            pressure = main['pressure']
        if lat is None:
            latitude = default_x['coord']
            lat = latitude['lat']
            long = latitude['lon']
        if description is None:
            description = default_x['weather'][0]['description']
    temprature_label = Label(root, fg=_from_rgb((0, 0, 153)), text=f'{temprature} Celsius',font=('Broadway', 20, 'bold'), bg=_from_rgb((73,183,232)))
    temprature_label.place(x=x/2.40, y=200)
    description_label = Label(root,bg=_from_rgb((73,183,232)), text=description,font=('Broadway', 15, 'bold'))
    description_label.place(x=x/2.33, y=238)
    get_coordinates = Label(root, bg=_from_rgb((73,183,232)), text=f'Coordinates {lat, long}')
    get_coordinates.place(x=x/2.35, y=275)
    get_pressure = Label(root, bg=_from_rgb((73,183,232)), text=f'Pressure {pressure} kpa')
    get_pressure.place(x=x/2.32, y=300)

make_default_window()


































root.mainloop()
