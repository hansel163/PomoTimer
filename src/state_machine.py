from transitions import Machine, State
from const import *


class TimerStateMachine(object):
    # Define timer states. 
    states = [State(name='stopped',  on_exit=['on_exit_stopped']), 'running',
             'paused', 'overflowed','alarmed']

    state_dict = {None: TimerState.Invalid,
                  'stopped': TimerState.Stopped,
                  'running': TimerState.Running,
                  'paused': TimerState.Paused,
                  'overflowed': TimerState.Overflowed,
                  'alarmed': TimerState.Alarmed}

    def __init__(self, timer):
        super().__init__()
        self.timer = timer

        self.prev_state = None
        self.machine = Machine(
            model=self, states=TimerStateMachine.states,
            initial='stopped')
        self.machine.add_transition(
            trigger='on_stop', source='*', dest='stopped',
            before='save_prev_state')
        
        self.machine.add_transition(
            trigger='on_pause', source=['running', 'alarmed'],
            dest='paused', before='save_prev_state')

        self.machine.add_transition(
            trigger='on_overflow',
            source=['running', 'alarmed'],
            dest='overflowed', before='save_prev_state')

        self.machine.add_transition(
            trigger='on_alarm', source='running',
            dest='alarmed', before='save_prev_state')
        
        self.machine.add_transition(
            trigger='on_start', source='paused',
            dest='alarmed', conditions='prev_is_alarmed',
            before='save_prev_state')

        self.machine.add_transition(
            trigger='on_start', source='paused',
            dest='running', conditions='prev_is_running',
            before='save_prev_state')

        self.machine.add_transition(
            trigger='on_start', source='stopped', dest='running',
            before='save_prev_state')

    def prev_is_alarmed(self):
        return self.prev_state == 'alarmed'
    
    def prev_is_running(self):
        return self.prev_state == 'running'

    def on_exit_stopped(self):
        self.timer.calc_step()

    def on_enter_stopped(self):
        self.timer.stop()
        self.timer.restore_timer()

    def on_enter_running(self):
        self.timer.start()

    def on_enter_paused(self):
        self.timer.pause()

    def on_enter_overflowed(self):
        self.timer.stop()

    def on_enter_alarmed(self):
        pass
   
    def save_prev_state(self):
        # self.state is created by transitions lib
        self.prev_state = self.state

    def get_state(self):
        return TimerStateMachine.state_dict[self.state]
    
    def get_prev_state(self):
        return TimerStateMachine.state_dict[self.prev_state]

def test():
    machine = TimerStateMachine()
    machine.on_start()
    print(machine.state)


if __name__ == '__main__':
    test()






