import tkinter as tk
import pygubu
import os
import Pyro4
from PositionUpdater import PositionUpdater

class Application:
    def __init__(self, master):
        self.master = master

        pyroUri = input("Enter Pyro uri: ").strip()
        self.loufchatz = Pyro4.Proxy(pyroUri)

        self.builder = pygubu.Builder()
        self.builder.add_from_file('client.ui')

        img_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.', 'images')
        img_path = os.path.abspath(img_path)
        self.builder.add_resource_path(img_path)

        self.mainwindow = self.builder.get_object('window', master)
        self.builder.connect_callbacks(self)

        pos = PositionUpdater(self.loufchatz, self)
        pos.start()

    def updatePosition(self, X, Z):
        TextFieldX = self.builder.get_object('PosX')
        TextFieldZ = self.builder.get_object('PosZ')
        TextFieldX.delete('1.0', tk.END)
        TextFieldX.insert(tk.INSERT, X)
        TextFieldZ.delete('1.0', tk.END)
        TextFieldZ.insert(tk.INSERT, Z)
        self.master.update()

    def on_BackwardFast_clicked(self):
        self.loufchatz.driveBackwardFast()

    def on_Backward_clicked(self):
        self.loufchatz.driveBackward()

    def on_BackwardSlow_clicked(self):
        self.loufchatz.driveBackwardSlow()

    def on_Stop_clicked(self):
        self.loufchatz.stop()

    def on_ForwardSlow_clicked(self):
        self.loufchatz.driveSlow()

    def on_Forward_clicked(self):
        self.loufchatz.drive()

    def on_ForwardFast_clicked(self):
        self.loufchatz.driveFast()

    def on_HopperDown_clicked(self):
        self.loufchatz.hopperDown()

    def on_HopperStop_clicked(self):
        self.loufchatz.hopperStop()

    def on_HopperUp_clicked(self):
        self.loufchatz.hopperUp()

    def on_AttachCube_clicked(self):
        self.loufchatz.attachCube()

    def on_ReleaseCube_clicked(self):
        self.loufchatz.releaseCube()

    def on_State_clicked(self):
        self.loufchatz.getState()

    def on_Reset_clicked(self):
        self.loufchatz.reset()


if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 2.0)
    app = Application(root)
    root.mainloop()
