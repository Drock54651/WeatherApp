import customtkinter as ctk
from settings import *
from main_widgets import *

#* URL request
import urllib.request
import json

#* WEATHER
from weather_data import get_weather

try:
    from ctypes import windll, byref, sizeof, c_int

except:
    pass


class App(ctk.CTk):
    def __init__(self):

        self.color = WEATHER_DATA['Clear']

        super().__init__(fg_color = self.color['main'])
        self.change_title_bar(self.color['title'])
        
        self.geometry('550x250')
        self.minsize(550,250)
        self.iconbitmap('empty.ico')
        self.title('')
        

        #* START WIDGET
        self.widget = SmallWidget(self)


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
            self.widget = MaxWidget(self)
        
        #* TALL WIDGET
        if self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = TallWidget(self)

        #* WIDE WIDGET
        if not self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = WideWidget(self)

        #* SMALL WIDGET
        if not self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = SmallWidget(self)



if __name__ == '__main__':

    #*LOCATION
    with urllib.request.urlopen("https://ipapi.co/json/") as url:
        data = json.loads(url.read().decode())
        city = data['city']
        country = data['country_name']
        latitude = data['latitude']
        longitude = data['longitude']

    #* WEATHER INFO
    current_data = get_weather(latitude, longitude, 'imperial', 'today')
    forecast_data = get_weather(latitude, longitude, 'imperial', 'forecast')
    print(forecast_data)

    App()