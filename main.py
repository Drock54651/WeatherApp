import customtkinter as ctk
from settings import *
from main_widgets import *
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
        self.configure('<Configure>', self.check_size)



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
            
            if self.full_width_bool.get(): #! if window width > 600 px
                
                if event.width < self.width_break:
                    self.full_width_bool.set(False)
            
            else: #! window < 600 px wide
                if event.width > self.width_break:
                    self.full_width_bool.set(True)
            





if __name__ == '__main__':
    App()