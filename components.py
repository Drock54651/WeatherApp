import customtkinter as ctk

class SimplePanel(ctk.ctkframe):
    def __init__(self, parent, weather, row, col, color):
        super().__init__(parent, fg_color = color['main'], corner_radius = 0)
        self.grid(row = row, col = col, sticky = 'news')