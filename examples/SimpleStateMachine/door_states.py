from state import State

class Opened(State):
    def __init__(self):
        print('Processing current state:', str(self))

    def on_event(self, event):
        if event == 'close':
            return Closed()
        return self

class Closed(State):
    def __init__(self):
        print('Processing current state:', str(self))

    def on_event(self, event):
        if event == 'open':
            return Opened()
        return self
