import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "hello world"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.lol = tk.Button(self)
        self.lol["text"] = "test"
        self.lol.pack()

        self.quit = tk.Button(self, text="QUit", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("fuck there")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
