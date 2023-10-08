from tkinter import Canvas
from PIL import ImageTk
class StaticImage(Canvas):
    def __init__(self, parent, forecast_images, row, col):
        super().__init__(parent, background= 'white', bd  = 0, highlightthickness = 0, relief = 'ridge', width = 100, height = 100)
        self.grid(row = row, column = col, sticky  = 'news')

        #* IMAGE RATIO
        self.image  = forecast_images
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_ratio = self.image.size[0] / self.image.size[1]

        #* Start values
        self.canvas_width = 0
        self.canvas_height = 0
        self.image_width = 0
        self.image_height = 0

        #* Event
        self.bind('<Configure>', self.resize)

    
    def resize(self, event = None):
        canvas_ratio = event.width / event.height

        self.canvas_width = event.width
        self.canvas_height = event.height

        #* Resize
        if canvas_ratio > self.image_ratio: #! canvas is wider than image
            self.image_height = int(self.canvas_height)
            self.image_width = int(self.image_height * self.image_ratio)

        else: #! canvas is taller than image
            self.image_width  = int(self.canvas_width)
            self.image_height = int(self.image_width * self.image_ratio)

        self.update_image()
    
    def update_image(self):
        self.delete('all')
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.create_image(self.canvas_width / 2, self.canvas_height / 2, image = self.image_tk)


