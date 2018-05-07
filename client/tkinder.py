import tkinter as tk
import pygubu
import os

class Application:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('client.ui')

        img_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.', 'images')
        img_path = os.path.abspath(img_path)
        builder.add_resource_path(img_path)

        self.mainwindow = builder.get_object('window', master)


if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 2.0)
    app = Application(root)
    root.mainloop()
