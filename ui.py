import tkinter as t


class AppInterface:
    def __init__(self):
        self.height = 600
        self.width = 900
        self.window = t.Tk()
        self.window.title("Time Machine")
        self.window.config(height=600, width=900)

        self.background_image = t.PhotoImage(file="images/img.png")
        self.canvas = t.Canvas(self.window, height= self.height,width= self.width)
        self.canvas.pack(fill="both", expand= True)
        self.canvas.create_image(self.width/2, self.height/2, image=self.background_image)

        self.window.mainloop()
