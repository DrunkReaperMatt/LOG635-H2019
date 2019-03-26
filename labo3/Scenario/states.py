from StateMachine.statemachine import State


class LockedState(State):
    def on_event(self, event):
        if event == 'test':
            return UnlockedState()

        return self


class UnlockedState(State):
    def on_event(self, event):
        if event == 'test done':
            return LockedState()

        return self
