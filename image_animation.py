from tkinter import Canvas
from PIL import ImageTk, Image
import customtkinter as ctk
class AnimatedImage(ctk.CTkLabel):
    def __init__(self, parent, images, row, col):
        self.images  = images
        self.frame_index = 0

        super().__init__(parent, text = '')
        self.grid(row = row, column = col, sticky  = 'news')

        self.animate()

    def update_image(self):
        weather_image = ctk.CTkImage(self.images[self.frame_index], size = (150,150))

        self.configure(text = '', image = weather_image)

    def animate(self):
        self.frame_index += 1
        if self.frame_index >= len(self.images):
            self.frame_index = 0

        self.update_image()
        self.after(42, self.animate) #! 1000 ms to play 24 frames, 1000 / 24 = 42, play animation in one second




#NOTE: Made this all much simpler in the above, albeit a little less flexible, can uncomment this below and commenting the above
# class AnimatedImage(Canvas):
#     def __init__(self, parent, images, row, col, color):
#         super().__init__(parent, background= color, bd  = 0, highlightthickness = 0, relief = 'ridge')
#         self.grid(row = row, column = col, sticky  = 'news')
    #     #* IMAGE RATIO
    #     self.images  = images
    #     self.frame_index = 0
    #     self.image_tk = ImageTk.PhotoImage(self.images[self.frame_index])
    #     self.image_ratio = self.images[self.frame_index].size[0] / self.images[self.frame_index].size[1]

    #     #* Start values
    #     self.canvas_width = 0
    #     self.canvas_height = 0
    #     self.image_width = 0
    #     self.image_height = 0

    #     #* Event
    #     self.bind('<Configure>', self.resize)
    #     self.animate()
    
    # def resize(self, event = None):
    #     canvas_ratio = event.width / event.height

    #     self.canvas_width = event.width
    #     self.canvas_height = event.height

    #     #* Resize
    #     if canvas_ratio > self.image_ratio: #! canvas is wider than image
    #         self.image_height = int(self.canvas_height)
    #         self.image_width = int(self.image_height * self.image_ratio)

    #     else: #! canvas is taller than image
    #         self.image_width  = int(self.canvas_width)
    #         self.image_height = int(self.image_width * self.image_ratio)

    #     self.update_image()
    
    # def update_image(self):
    #     self.delete('all')

    #     if(self.image_width, self.image_height) != (0,0):
    #         resized_image = self.images[self.frame_index].resize((self.image_width, self.image_height))
    #         self.image_tk = ImageTk.PhotoImage(resized_image)
    #         self.create_image(self.canvas_width / 2, self.canvas_height / 2, image = self.image_tk)

    # def animate(self):
    #     self.frame_index += 1
    #     if self.frame_index >= len(self.images):
    #         self.frame_index = 0

    #     self.update_image()
    #     self.after(42, self.animate) #! 1000 ms to play 24 frames, 1000 / 24 = 42, play animation in one second
        