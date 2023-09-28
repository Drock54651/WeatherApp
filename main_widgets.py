from customtkinter import CTkFrame

#! Accounts for resizing the window
#! Depending on size, layout and information shown will be different

class SmallWidget(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'red')
        self.pack(expand = True, fill = 'both')

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