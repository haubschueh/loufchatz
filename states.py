#The basic State provides a method to describe itself.
class State:
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

class WaitForStartSignal(State):
    def __init__(self):
        pass

    def on_event(self, event):
        if event == 'signalReceived':
            return TakeUpCube()
        return self

class TakeUpCube:
    def __init__(self):
        pass

    def on_event(self, event):
        if event == 'cubeLifted':
            return ScanForTarget()
        return self

class ScanForTarget:
    def __init__(self):
        pass

    def on_event(self, event):
        if event == 'targetFound':
            return AlignAboveTarget()
        return self

class AlignAboveTarget:
    def __init__(self):
        pass

    def on_event(self, event):
        if event == 'positioningFinished':
            return FinishParcour()
        return self

class FinishParcour:
    def __init__(self):
        pass

    def on_event(self, event):
        if event == 'end':
            return 0
        return self
