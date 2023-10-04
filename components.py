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
        ctk.CTkLabel(temp_frame, text = f'{weather["temp"]}', font  = ctk.CTkFont(family = 'Calibri', size = 50), text_color = color['text']).pack()
        ctk.CTkLabel(temp_frame, text = f'feels like {weather["feels_like"]}', font  = ctk.CTkFont(family = 'Calibri', size = 16), text_color = color['text']).pack()
        temp_frame.grid(row = 0, column = 0)