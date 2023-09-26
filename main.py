import customtkinter as ctk
from settings import *
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
        



        #* RUN
        self.mainloop()
    

    def change_title_bar(self, color):
        try:

            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(color)), sizeof(c_int))

        except:
            pass

if __name__ == '__main__':
    App()