import customtkinter as ctk
from settings import *
from main_widgets import *

#* URL request
import urllib.request
import json

#* WEATHER
from weather_data import get_weather

from PIL import Image

try:
    from ctypes import windll, byref, sizeof, c_int

except:
    pass


class App(ctk.CTk):
    def __init__(self, current_data, forecast_data, city, country):

        self.current_data = current_data
        print(self.current_data)
        self.forecast_data = forecast_data
        self.location = {'city': city, 'country': country}
        self.color = WEATHER_DATA[current_data['weather']]

        self.forecast_images = [Image.open(f"images/{info['weather']}.png") for info in self.forecast_data.values()] #! gets values of the dict

        super().__init__(fg_color = self.color['main'])
        self.change_title_bar(self.color['title'])
        
        self.geometry('550x250')
        self.minsize(550,250)
        self.iconbitmap('empty.ico')
        self.title('')
        

        #* START WIDGET
        self.widget = SmallWidget(self, self.current_data, self.location, self.color)


        #* STATES
        self.height_break = 600
        self.width_break = 1000
    
        self.full_height_bool = ctk.BooleanVar(value = False) #! checks if window size exceeds the height break of 600px
        self.full_width_bool = ctk.BooleanVar(value = False)  #! Check width break
        self.bind('<Configure>', self.check_size)
        self.full_width_bool.trace('w', self.change_size)
        self.full_height_bool.trace('w', self.change_size)



        #* RUN
        self.mainloop()
    

    def change_title_bar(self, color):
        try:

            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(color)), sizeof(c_int))

        except:
            pass


    def check_size(self, event):
        if event.widget == self: #! prevents calling configure on every widget, this ensures only the main window is applied
            
            #* WIDTH
            if self.full_width_bool.get(): #! if window width > 1000 px, check if the width becomes smaller or equal to 1000
                if event.width < self.width_break:
                    self.full_width_bool.set(False)
            
            else: #! window width < 1000 px, check if the width becomes bigger or equal to 1000
                if event.width > self.width_break:
                    self.full_width_bool.set(True)

            #* HEIGHT
            if self.full_height_bool.get(): #! if window height > 600 px
                if event.height < self.height_break:
                    self.full_height_bool.set(False)
            
            else: #! window height < 600 px 
                if event.height > self.height_break:
                    self.full_height_bool.set(True)

    def change_size(self, *args):
        self.widget.pack_forget()

        #* MAX WIDGET
        if self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = MaxWidget(self, 
                                    current_data = self.current_data, 
                                    location = self.location, 
                                    forecast_data = self.forecast_data, 
                                    color = self.color,
                                    forecast_images = self.forecast_images)
        
        #* TALL WIDGET
        if self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = TallWidget(self, 
                                     current_data = self.current_data, 
                                     location = self.location, 
                                     forecast_data = self.forecast_data, 
                                     color = self.color,
                                     forecast_images = self.forecast_images)

        #* WIDE WIDGET
        if not self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = WideWidget(self, 
                                     current_data = self.current_data, 
                                     location = self.location, 
                                     forecast_data = self.forecast_data, 
                                     color = self.color,
                                     forecast_images = self.forecast_images)

        #* SMALL WIDGET
        if not self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = SmallWidget(self, self.current_data, self.location, self.color)



if __name__ == '__main__':

    #*LOCATION
    with urllib.request.urlopen("https://ipapi.co/json/") as url:
        data = json.loads(url.read().decode())
        
        city = data['city']
        country = data['country_name']
        latitude = data['latitude']
        longitude = data['longitude']

    #* WEATHER INFO
    #! Will return dictionary of temp, feellike, and weather
    current_data = get_weather(latitude, longitude, 'imperial', 'today')
    forecast_data = get_weather(latitude, longitude, 'imperial', 'forecast')

    App(current_data = current_data, forecast_data = forecast_data, city  = city, country  = country)