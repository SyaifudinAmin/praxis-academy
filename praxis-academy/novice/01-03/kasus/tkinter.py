from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.text()
        # label(self)

    def init_window(self):
        #changing tittle 
        self.master.title("CRC")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit")

        # placing the button on my window
        quitButton.place(x=340, y=260)

    def text(self):
        label1 = Label(self, text = "Test my Text")
        label1.place(x=0,y=0) 
        label2 = Label(self, text = "my next label")
        label2.place(x=20,y=20)


root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()
# ------------------------------------------------------------------------------------
# main_window = tkinter.Tk()


# label1 = tkinter.Label(main_window, text = "First Label")

# # method position
# label1.pack()

# main_window.mainloop()
# ------------------------------------------------------------------------------------
# import tkinter as tk

# class ApplicationCRC(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi = tk.Button()
#         self.hi ["text"] = "Heloo(click)"
#         self.hi ["command"] = self.say_hi
#         self.hi.pack(side="top")

#         self.quit = tk.Button (self, text=("Exit"), fg="red", command = self.master.destroy)
#         self.quit.pack(side= "bottom")

#     def say_hi(self):
#         print("Hiiii")

# root = tk.Tk()
# app = ApplicationCRC(master=root)
# app.mainloop()