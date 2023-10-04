import customtkinter as ctk

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
                     font  = ctk.CTkFont(family = 'Calibri', size = 20), 
                     text_color = color['text']).pack(side = 'left')
        
        location_frame.pack(side = 'left', padx = 10)
        #* DATE