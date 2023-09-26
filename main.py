import customtkinter as ctk

try:
    from ctypes import windll

except:
    pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1000x600')
        self.iconbitmap('empty.ico')
        self.title('')
        


        #* RUN
        self.mainloop()
    

    def change_title_bar

App()