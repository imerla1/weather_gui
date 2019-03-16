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
import tkinter as tk
from tkinter import Text
from time import strftime
import time
from datetime import datetime as dt
from time import sleep
from default_distance import default_distance, travel_time

# Loading Screen Section


'''def task():
    # The window will stay open until this function call ends.
    sleep(5)  # Replace this with the code you want to run
    Loading_screen.destroy()


Loading_screen = tk.Tk()
Loading_screen.title("Weather For life")
Loading_screen.attributes("-fullscreen", True)
x_ = Loading_screen.winfo_screenwidth()
y_ = Loading_screen.winfo_screenheight()
size = x_, y_
im = Image.open("load.png")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("main_loading.png", "PNG")
new_im = ImageTk.PhotoImage(Image.open('main_loading.png'))
load_label = Label(Loading_screen, image=new_im)
load_label.pack()

Loading_screen.after(200, task)
Loading_screen.mainloop()'''


# required to make window show before the program gets to the mainloop

# From there starts Main window
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


root = tk.Tk()


root.title('Weather')
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
time_var = StringVar()
date_var = StringVar()


def set_time():
    time_var.set(strftime('%H:%M:%S'))
    root.after(1000, set_time)


def set_date():
    now = dt.now()
    formated = f'{now.month}/{now.day}/{now.year}'
    date_var.set(formated)


def set_location_to_map():
    try:
        map_hooray = folium.Map(location=[lat, long],

                                zoom_start=12)
        folium.Marker([lat, long]).add_to(map_hooray)

        map_hooray.save('index.html')
        webbrowser.open('file://' + os.path.realpath('index.html'))
    except:
        if len(main_entry.get()) != 0:
            messagebox.showwarning('Warning!!', 'Country or city name\nis incorrect')
        if len(main_entry.get()) == 0:
            messagebox.showerror('Error', 'Pls enter city or\nCountry name')


def settings():  # TODO: Settings Button
    pass

def check_map():
    Tbilisi = (41.69, 44.8)
    points = [Tbilisi, (lat, long)]
    my_map = folium.Map(location=Tbilisi, zoom_start=5)
    for j in points:
        folium.Marker(j).add_to(my_map)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(my_map)
    my_map.save('index.html')
    webbrowser.open('file://' + os.path.realpath('index.html'))


'''def distance_():
    app = Info()
    app.get_personal_info()
    from_addr = app.city
    to_addrs = main()
    unformated = 'https://www.distance24.org/route.json?stops={}|{}'.format(from_addr, to_addrs)
    req_ = requests.get(unformated)
    dw = req_.json()
    distance = dw['distance']
    return distance'''

# Canvas Sector
# Canvas For Current Information
# Background Canvas For information
main_canvas = Canvas(root, width=x-300, height=y-30)
main_canvas.place(x=300, y=30)
back_image = ImageTk.PhotoImage(Image.open('try3.jpg'))
main_canvas.create_image(1500, 300, image=back_image)
Label(root, bd=11, textvariable=time_var, font='Verdana 32 bold italic',
      bg=_from_rgb((15, 20, 49)), fg='white').place(x=x-270, y=25)
Label(root, bd=11, textvariable=date_var, font='Verdana 10 bold italic',
      bg=_from_rgb((15, 20, 49)), fg='white').place(x=x-200, y=90)
#moon_img = ImageTk.PhotoImage(Image.open('sunny.png'))
#main_canvas.create_image(x-700, 300, image=moon_img)
mytime = time.localtime()
if mytime.tm_hour < 6 or mytime.tm_hour > 18:
    moon_img = ImageTk.PhotoImage(Image.open('moon_main.png'))
    main_canvas.create_image(x-700, 300, image=moon_img)
else:
    sunny_img = ImageTk.PhotoImage(Image.open('sunny.png'))
    main_canvas.create_image(x-700, 300, image=sunny_img)
# Canvas For Current Information child for background Canvas

curr_canvas = Canvas(main_canvas, width=370, height=220)
curr_canvas.place(x=10, y=500)
current_image = ImageTk.PhotoImage(Image.open('current.png'))
curr_canvas.create_image(182, 12, image=current_image)
curr_canvas.create_text(70, 80, text='humidity', font="Helvetica 15 bold",
                        fill=_from_rgb((50, 50, 50)))  # humidity text
curr_canvas.create_text(83, 115, text='wind speed', font="Helvetica 15 bold",
                        fill=_from_rgb((50, 50, 50)))  # Wind speed
curr_canvas.create_text(70, 150, text='pressure', font="Helvetica 15 bold",
                        fill=_from_rgb((50, 50, 50)))  # pressure

# Canvas For Personal Information child for background Canvas
personal_canvas = Canvas(main_canvas, width=370, height=220)
personal_canvas.place(x=420, y=500)
personal_info_img = ImageTk.PhotoImage(Image.open('pers_info1.png'))
personal_canvas.create_image(265, 12, image=personal_info_img)
# Canvas For Distance Between your country and Endpoint child for background Canvas
distance_canvas = Canvas(main_canvas, width=370, height=220)
distance_canvas.place(x=827, y=500)
distance_header = ImageTk.PhotoImage(Image.open('distance_header.png'))
distance_canvas.create_image(195, 15, image=distance_header)


def personal_window():
    parse = Info().get_personal_info()
    x_axis = 60
    x_axis2 = 215
    y_axis = 35
    for k, v in parse.items():
        personal_canvas.create_text(x_axis, y_axis, text=f'{k}')
        personal_canvas.create_text(x_axis2, y_axis, text=f'{v}')
        y_axis += 15


# Seach Canvas
scanvas = Canvas(root, width=300, height=y-30, bg=_from_rgb((59, 58, 60)))
scanvas.place(x=0, y=30)

# Upper canvas For logo and Menu

menu_canvas = Canvas(root, width=x, height=30, bg='blue')
menu_canvas.place(x=0, y=0)
main_logo = ImageTk.PhotoImage(Image.open('mainlogo.png'))
menu_canvas.create_image(x/2, 15, image=main_logo)

# City Country Search Entry
large_font = ('Helvetica', 13)
city_names = StringVar()
main_entry = Entry(scanvas, textvariable=city_names, font=large_font, width=15,
                   fg=_from_rgb((255, 255, 255)), bg=_from_rgb((137, 137, 138)),
                   relief=SOLID,
                   highlightcolor='red',
                   selectforeground='white',
                   )
main_entry.place(x=30, y=50)
city_names.set("Enter Location")
# main Function for search Button


def main():
    try:
        global x
        x = main_entry.get()
        url_base = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        APIKEY = '3fcb9950908ddd9b5672e2a29e4842a2'
        req = requests.get(url_base.format(x, APIKEY))
        response = req.json()
        country = response['sys']['country']

        city = response['name']
        global lat
        global long
        temprature = None
        city_country = None
        lat = None
        long = None
        description = None
        pressure = None
        humidity = None
        wind_speed = None
        for j in response:
            main = response['main']
            if temprature is None:
                temprature = round(main['temp'] - 273.15, 2)
            if pressure is None:
                pressure = main['pressure']
            if lat is None:
                coords = response['coord']
                lat = coords['lat']
                long = coords['lon']
            if description is None:
                description = response['weather'][0]['description']
            if humidity is None:
                humidity = main['humidity']
            if wind_speed is None:
                wind_speed = response['wind']['speed']
        url_format = 'https://www.distance24.org/route.json?stops={}|{}'
        distance_request = requests.get(url_format.format('Tbilisi', city))
        distance_respones = distance_request.json()
        new_dist = distance_respones['distance']
        print(new_dist)

        main_canvas.itemconfig(w, text=f'{city}, {country} ({lat}, {long})')
        main_canvas.itemconfig(des, text=f'{description}')
        main_canvas.itemconfig(te, text=f'{temprature}{chr(176)}C')
        curr_canvas.itemconfig(humidity_can, text=f'{humidity}%')
        curr_canvas.itemconfig(wind_can, text=f'{wind_speed} M/S')
        curr_canvas.itemconfig(press_can, text=f'{pressure} Hpa')
        distance_canvas.itemconfig(dist_addr_canv, text=f'{new_dist} KM')
        distance_canvas.itemconfig(to_addr_canv, text=f' To {city} ')
        distance_canvas.itemconfig(travel_time, text=f'{round(new_dist/800, 2)} Hour')
    except:
        messagebox.showerror('Error!', 'OOPS please Enter Country\n or city name corectly')


    # Search Button
search_button = Button(scanvas, bg=_from_rgb((255, 102, 0)), command=main)
search_img = ImageTk.PhotoImage(Image.open('search1.png'))
search_button.config(image=search_img)
search_button.place(x=180, y=47)
# Settings Button
setting_button = Button(scanvas, bg=_from_rgb((59, 58, 60)))
setting_img = ImageTk.PhotoImage(Image.open('32.png'))
setting_button.config(image=setting_img)
setting_button.place(x=30, y=y-160)
# Check on folium map Button
check_on_map = ttk.Button(distance_canvas, text='Check on map', command=check_map)
check_on_map.place(x=120, y=180)
# Country code for better result text
text = 'Add the country code for better results.\n \tEx: London, UK'
scanvas.create_text(130, 95, text=text, fill=_from_rgb((0, 204, 255)),
                    font="Helvetica 10 bold")


def make_default_window():
    global obj
    obj = Info()
    obj.get_personal_info()
    url_base = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    APIKEY = '3fcb9950908ddd9b5672e2a29e4842a2'
    global city_name
    global travel_time
    global dist_addr_canv
    city_name = obj.city
    country_name = obj.country
    global w  # Country lat long canvas
    global des  # Country desc
    global te  # Country temprature
    global to_addr_canv
    # Current Canvas
    global humidity_can
    global wind_can
    global press_can
    #######
    '''global humidity
    global wind_speed # meter second m/s
    global temprature
    global city_country
    global lat
    global long
    global description'''

    req = requests.get(url_base.format(city_name, APIKEY))

    response = req.json()
    temprature = None

    lat = None
    long = None
    description = None
    pressure = None
    humidity = None
    wind_speed = None
    for j in response:
        main = response['main']
        if temprature is None:
            temprature = round(main['temp'] - 273.15, 2)
        if pressure is None:
            pressure = main['pressure']
        if lat is None:
            coords = response['coord']
            lat = coords['lat']
            long = coords['lon']
        if description is None:
            description = response['weather'][0]['description']
        if humidity is None:
            humidity = main['humidity']
        if wind_speed is None:
            wind_speed = response['wind']['speed']

    w = main_canvas.create_text(200, 35,
                                text=f'{city_name}, {country_name} ({lat}, {long})',
                                font="Helvetica 20 bold",
                                fill=_from_rgb((255, 255, 255)))
    des = main_canvas.create_text(200, 300,
                                  text=f'{description}',
                                  font="Helvetica 25 bold",
                                  fill=_from_rgb((255, 255, 255))
                                  )
    te = main_canvas.create_text(200, 380,
                                 text=f'{temprature}{chr(176)}C',
                                 font="Helvetica 60 bold",
                                 fill=_from_rgb((255, 255, 255))
                                 )
    humidity_can = curr_canvas.create_text(300, 80,
                                           text=f'{humidity}%',
                                           font="Helvetica 15 bold",
                                           fill=_from_rgb((50, 50, 50))
                                           )
    wind_can = curr_canvas.create_text(300, 115,
                                       text=f'{wind_speed} M/S',
                                       font="Helvetica 15 bold",
                                       fill=_from_rgb((50, 50, 50))
                                       )
    press_can = curr_canvas.create_text(300, 150,
                                        text=f'{pressure} Hpa',
                                        font="Helvetica 15 bold",
                                        fill=_from_rgb((50, 50, 50))
                                        )
    distance_canvas.create_text(100, 70,
                                        text=f'from {city_name}   -',
                                        font="Helvetica 15 bold",
                                        fill=_from_rgb((50, 50, 50))
                                        )
    to_addr_canv = distance_canvas.create_text(240, 70,
                                        text='To Moscow',
                                        font="Helvetica 15 bold",
                                        fill=_from_rgb((50, 50, 50))
                                        )
    dist_addr_canv = distance_canvas.create_text(180, 110,
                                        text=f'{default_distance()} KM',
                                        font="Helvetica 15 bold",
                                        fill=_from_rgb((50, 50, 50))
                                        )
    distance_canvas.create_text(125, 160,
                                        text='travel time with plane:',
                                        font="Helvetica 15 bold",
                                        fill=_from_rgb((50, 50, 50))
                                        )
    travel_time = distance_canvas.create_text(287, 160, text=f'{default_distance()/800} Hour',
                                                font="Helvetica 15 bold")

if __name__ == '__main__':

    make_default_window()
    personal_window()
    set_time()
    set_date()

    # set_location_to_map()
    root.mainloop()
