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
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'blue')
        self.pack(expand = True, fill = 'both')


class TallWidget(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'Green')
        self.pack(expand = True, fill = 'both')

class MaxWidget(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'yellow')
        self.pack(expand = True, fill = 'both')