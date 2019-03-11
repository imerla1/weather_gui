from tkinter import *
from PIL import ImageTk,Image
import requests
import json
from main import get_info, kelvin_to_celsius, temprature, pressure, lat, long, description
from tkinter import messagebox

root = Tk()
root.geometry('1000x1000')
root.title('weather App')
img = ImageTk.PhotoImage(Image.open('weather.png'))
panel = Label(root,image=img)
panel.place(x=375,y=45)
lable_0 = Label(root,text="Weather App",width = 20,font=("bold",20),fg='red')
lable_0.place(x=340,y=2)

city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names)
city_names.set("Enter City Here ...")
entry_1.place(x=425, y=350)


att = '...'
# Labels
lat_long = Label(root, text='lat, long', fg='blue').place(x=370, y=540)
temp_label = Label(root, text='Temprature:', fg='blue').place(x=370, y=450)
pressure_label = Label(root, text='Pressure:', fg='blue').place(x=370, y=480)
description_label = Label(root, text='Description:', fg='blue').place(x=370, y=510)
temp1_label_ = Label(root, text=att, fg='blue')
temp1_label_.place(x=460, y=450)
pressure1_label_ = Label(root, text=att, fg='blue')
pressure1_label_.place(x=460, y=480)
description1_label_ = Label(root, text=att, fg='blue')
description1_label_.place(x=460, y=510)
lat_long_ = Label(root, text=att, fg='blue')
lat_long_.place(x=460, y=540)

# Checkboxes
def get_cel():
    temp1_label_.configure(text='{} Celsius'.format(temprature))

def get_kelvin():
    temp1_label_.configure(text='{} Kelvin'.format(temprature+273.15))

def get_fare():
    temp1_label_.configure(text='{} Farenheit'.format(temprature * 9/5 +32))


check_button_c = Checkbutton(root, text='Celsius', command=get_cel)
check_button_c.place(x=500 , y=450)
check_button_k = Checkbutton(root, text='kelvin', command=get_kelvin)
check_button_k.place(x=580 , y=450)
check_button_f = Checkbutton(root, text='Farenheit', command=get_fare)
check_button_f.place(x=660 , y=450)



def get_name():
    name = entry_1.get()
    url_base = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    APIKEY = '3fcb9950908ddd9b5672e2a29e4842a2'
    try:
        req = requests.get(url_base.format(name, APIKEY))
        x = req.json()
        global temprature
        temprature = None
        pressure = None
        lat, long = None, None
        description = None


        for j in x:
            main = x['main']
            if temprature is None:
                temprature = round(main['temp'] -273.15, 2)
            if pressure is None:
                pressure = main['pressure']
            if lat is None:
                latitude = x['coord']
                lat = latitude['lat']
                long = latitude['lon']
            if description is None:
                description = x['weather'][0]['description']


        temp1_label_.configure(text='{} Celsius'.format(temprature))
        pressure1_label_.configure(text='{} Kpa'.format(pressure))
        description1_label_.configure(text=description)
        lat_long_.configure(text='{} lat {} long'.format(lat, long))
        check_button_c.place(x=550 , y=450)
        check_button_k.place(x=620 , y=450)
        check_button_f.place(x=680 , y=450)
    except Exception:
        temp1_label_.configure(text='errr')
        pressure1_label_.configure(text='errr')
        description1_label_.configure(text='errr')
        lat_long_.configure(text='errr')
        messagebox.showerror('Error!', 'Check Apikey or Countryname may be incorect')









enter_button = Button(root, text='click', width=10, command=get_name, bg='green')
enter_button.place(x=440, y=380)


root.mainloop()
