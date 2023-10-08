from customtkinter import CTkFrame
from components import *

#! Accounts for resizing the window
#! Depending on size, layout and information shown will be different

class SmallWidget(CTkFrame):
    def __init__(self, parent, current_data, location, color):
        super().__init__(parent, fg_color = 'transparent')

        self.pack(expand = True, fill = 'both')

        #* LAYOUT
        self.rowconfigure(0, weight = 6, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        #* WIDGETS
        SimplePanel(self, current_data, 0, 0, color)
        DatePanel(self, location, row = 1, col = 0, color = color)


class WideWidget(CTkFrame):
    def __init__(self, parent, current_data, forecast_data, location, color):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')

        #* LAYOUT
        self.rowconfigure(0, weight = 6, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a') 
        self.columnconfigure(1, weight = 2, uniform = 'a') 

        #* WIDGETS
        SimplePanel(self, current_data, 0, 0, color)
        DatePanel(self, location, row = 1, col = 0, color = color)
        HorizontalForecastPanel(self, forecast_data, 0, 1, 2, color['divider color']) #! row, col, rowspan for the #s

class TallWidget(CTkFrame):
    def __init__(self, parent, current_data, forecast_data, location, color):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')

        #* Layout
        self.rowconfigure(0, weight = 3, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        #* WIDGET
        HorizontalForecastPanel(self, forecast_data, 1, 0, 1, color['divider color'])
        SimpleTallPanel(self, current_data, location, 0, 0, color)

class MaxWidget(CTkFrame):
    def __init__(self, parent, current_data, forecast_data, location, color):
        super().__init__(parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')
        
        #* Layout
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        #* WIDGETS
        SimpleTallPanel(self, current_data, location, 0, 0, color)
        VerticalForecastPanel(self, forecast_data, 0, 1, color['divider color'])