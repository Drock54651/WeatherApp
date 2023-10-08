import customtkinter as ctk
import datetime, calendar
from PIL import Image, ImageTk
class SimplePanel(ctk.CTkFrame):
    def __init__(self, parent, weather, row, col, color):
        super().__init__(parent, fg_color = color['main'], corner_radius = 0)
        self.grid(row = row, column = col, sticky = 'news')

        #* LAYOUT
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        #* WIDGETS
        temp_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        ctk.CTkLabel(temp_frame, text = f'{weather["temp"]}\N{DEGREE SIGN}', font  = ctk.CTkFont(family = 'Calibri', size = 50), text_color = color['text']).pack()
        ctk.CTkLabel(temp_frame, text = f'feels like {weather["feels_like"]}\N{DEGREE SIGN}', font  = ctk.CTkFont(family = 'Calibri', size = 16), text_color = color['text']).pack()
        temp_frame.grid(row = 0, column = 0)

class SimpleTallPanel(ctk.CTkFrame):
    def __init__(self, parent, weather_data, location, row, col, color):
        super().__init__(parent, fg_color = color['main'])
        self.grid(row = row, column = col, sticky = 'news')

        day, weekday, suffix, month = get_time_info() #! time info

        #* Layout 
        #! need 3 rows : location, image, temps
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 3, uniform = 'a')
        self.rowconfigure(2, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        #* LOCATION AND DATE FRAME
        location_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        
        location_frame.grid(row = 0, column = 0)
        ctk.CTkLabel(location_frame, #! location
                     text = f"{location['city']}, {location['country']}", 
                     font = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'), 
                     text_color = color['text']).pack()
        
        ctk.CTkLabel(location_frame, #! date
                     text = f'{weekday[:3]}, {day}{suffix} {calendar.month_name[month]}',
                     font  = ctk.CTkFont(family = 'Calibri', size = 20),
                     text_color = color['text']).pack()
        
        #* WEATHER IMAGE FRAME
        weather_image = ctk.CTkImage(Image.open(f"images/{weather_data['weather']}.png"), size = (100,100))
        ctk.CTkLabel(self, text = '', image  = weather_image).grid(row = 1, column = 0, sticky = 'news')


        #* TEMP FRAME
        temp_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        temp_frame.grid(row = 2, column  = 0)
        ctk.CTkLabel(temp_frame, 
                     text = f'{weather_data["temp"]}\N{DEGREE SIGN}', 
                     font = ctk.CTkFont(family = 'Calibri', size = 50),
                     text_color = color['text']).pack()
        
        ctk.CTkLabel(temp_frame, 
                     text = f'feels like: {weather_data["feels_like"]}\N{DEGREE SIGN}', 
                     font = ctk.CTkFont(family = 'Calibri', size = 16),
                     text_color = color['text']).pack()


class DatePanel(ctk.CTkFrame):
    def __init__(self, parent, location, row, col, color):
        super().__init__(parent, fg_color = color['main'], corner_radius = 0)
        self.grid(row = row, column = col, sticky = 'news')

        #* LOCATION
        location_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        ctk.CTkLabel(location_frame, 
                     text = f"{location['city']}, ", 
                     font  = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'), 
                     text_color = color['text']).pack(side = 'left')
        
        ctk.CTkLabel(location_frame, 
                     text = f"{location['country']}", 
                     font  = ctk.CTkFont(family = 'Calibri', size = 20, weight = 'bold'), 
                     text_color = color['text']).pack(side = 'left')
        
        location_frame.pack(side = 'left', padx = 10)

        #* DATE
        day, weekday, suffix, month = get_time_info()
        ctk.CTkLabel(self, 
                     text = f'{weekday[:3]}, {day}{suffix} {calendar.month_name[month]}',
                     font  = ctk.CTkFont(family = 'Calibri', size = 20),
                     text_color = color['text']).pack(side = 'right', padx = 10)

class HorizontalForecastPanel(ctk.CTkFrame):
    def __init__(self, parent, forecast_data, row, col, row_span, divider_color):
        super().__init__(parent, fg_color = '#FFF')
        self.grid(row = row, column = col, rowspan = row_span, sticky = 'news', padx = 6, pady = 6)
        

        #* WIDGETS
        for index, info in enumerate(forecast_data.items()):
            year, month, day = info[0].split('-')
            weekday = calendar.day_name[datetime.date(int(year), int(month), int(day)).weekday()][:3]
            frame = ctk.CTkFrame(self, fg_color = 'transparent')
            
            #* LAYOUT
            frame.columnconfigure(0, weight = 1, uniform = 'a')
            frame.rowconfigure(0, weight = 5, uniform = 'a')
            frame.rowconfigure(1, weight = 2, uniform = 'a')
            frame.rowconfigure(2, weight = 1, uniform = 'a')
                                    
            #* WIDGETS
            ctk.CTkLabel(frame, text = f"{info[1]['temp']}\N{DEGREE SIGN}", text_color = '#444', font = ('Calibri', 22)).grid(row = 1, column = 0, sticky = 'n')
            ctk.CTkLabel(frame, text = weekday, text_color = '#444').grid(row = 2, column = 0)
            frame.pack(side = 'left', expand = True, fill = 'both', padx = 5, pady = 5)

            if index != len(forecast_data) - 1:
                ctk.CTkFrame(self, fg_color = divider_color, width = 2).pack(side = 'left', fill = 'both')

class VerticalForecastPanel(ctk.CTkFrame):
    def __init__(self, parent, forecast_data, row, col, divider_color):
        super().__init__(parent, fg_color = '#FFF')
        self.grid(row = row, column = col, sticky = 'news', padx = 6, pady = 6)

        for index, info in enumerate(forecast_data.items()):
            year, month, day = info[0].split('-')
            weekday = calendar.day_name[datetime.date(int(year), int(month), int(day)).weekday()]

            frame = ctk.CTkFrame(self, fg_color = 'transparent')
            frame.pack(expand = True, fill = 'both', pady = 10)

            #* LAYOUT
            frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
            frame.rowconfigure(0, weight = 1, uniform = 'a')
            
            #* WIDGETS
            ctk.CTkLabel(frame, text = f"{info[1]['temp']}\N{DEGREE SIGN}", text_color = '#444', font = ('Calibri', 22)).grid(row = 0, column = 2, sticky = 'news')
            ctk.CTkLabel(frame, text = weekday, text_color = '#444').grid(row = 0, column = 0, sticky = 'news')

            if index != len(forecast_data) - 1:
                ctk.CTkFrame(self, fg_color = divider_color, height = 2).pack(fill = 'x')

def get_time_info():
    day = datetime.datetime.today().day 
    month = datetime.datetime.today().month 
    weekday = calendar.day_name[datetime.datetime.today().weekday()]

    match day % 10:
        case 1: suffix  = 'st'
        case 2: suffix  = 'nd'
        case 3: suffix = 'rd'
        case _: suffix = 'th'

    return day, weekday, suffix, month