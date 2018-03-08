from state import State

class Opened(State):
    def on_event(self, event):
        if event == 'close':
            return Closed()
        return self

class Closed(State):
    def on_event(self, event):
        if event == 'open':
            return Opened()
        return self