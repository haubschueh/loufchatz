from door_states import Opened

class Door():
    def __init__(self):
        self.state = Opened()

    def open(self):
        self.state = self.state.on_event('open')

    def close(self):
        self.state = self.state.on_event('close')