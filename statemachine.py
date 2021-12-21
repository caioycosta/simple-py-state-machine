# simple ND (depth-first) state machine
class State(object):
    def __init__(self, action, id="no-id"):
        self.id = id
        self.action = action
        self.transitions = []
        self._e = []
    
    def transition(self, condition_evaluator, next):
        self._e.append(self)
        while len(self._e):                
            self._e.pop().transitions.append( (condition_evaluator, next) )
        
    def start(self):
        self.action()
        next_states = []
        for t in self.transitions:            
            if t[0]():                
                next_states.append(t[1])
        for p in next_states:
            p.start()
    
    # used to combine transitions to be the same 
    def and_(self, est):
        self._e.append(est)
        return self
        
        
#    start_state = State(lambda: do_action())    
#    state_a = State(action_func)
#    state_b = State(action_func_b)
#    state_c = State(action_func_c)
#
#    # end state should be empty
#    end = State()
#    
#    start_state.transition(lambda: True, state_a) 
#    state_a.transition(lambda: condition1(), state_b)
#    state_a.transition(lambda: condition2(), end)
#
#    # set the same transition to two or more states by chaining and_
#    state_b.and_(state_c).transition(lambda: True, end)
#
#    # start the machine    
#    start_state.start()
