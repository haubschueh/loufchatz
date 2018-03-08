from door_states import Opened

class door(object):
    def __init__(self):
        self.state = LockedState()

    def open(self):
        self.state = self.state.on_event('open')

    def close(self):
        self.state = self.state.on_event('close')