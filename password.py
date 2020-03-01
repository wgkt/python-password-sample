#Deomnstrate how to use a class with tkinter

from tkinter import *

class Application(Frame):
    """A GUI application w three buttons."""

    #Constructor
    def __init__(self, master):
        """Inititializes the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.instruction = Label(self, text = "Enter the password")

        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, sticky = W)

        self.submit = Button(self, text = "Submit", command = self.reveal)
        self.submit.grid(row = 2, column =0, sticky = W)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        """display message based on the password typed"""
        content = self.password.get()
        if content == "password":
            message = "Access allowed"
        else:
            message = "Access denied"
        self.text.insert(0.0, message)
        #0.0 is poisition in row.column




        
root = Tk()
root.title("Password")
root.geometry("200x85")

app = Application(root)
root.mainloop()
