"""
    Ragnarok is a lighweight class for managing States with inmutability
    Developer: carlosaguilarnet@gmai.com
"""
class Ragnarok (object):

    """
    Constructor to initialize class
    @memberOf Ragnarok
    @constructor
    @param {self} self This class
    """
    def __init__(self):
        self.state = {}
        self.onUpdateHook = None
        self.stateless = 1

    """
    Initial state creation by developer
    @memberOf Ragnarok
    @public
    @param {self} self This class
    @param {Dictionary} _state Enter a dictionary as initial state
    """
    def setInitialState(self, _state):
        if (self.stateless == 0):
            return None

        self.__hookNotifier(_state, self.state)
        self.state = _state
        self.stateless = 0

    """
    Update state of the application
    @memberOf Ragnarok
    @public
    @param {self} self This class
    @param {Dictionary} _state Enter a dictionary of the state updated
    """
    def updateState (self, _state):
        oldState = self.state
        newState = oldState.copy()
        newState.update(_state)
        self.state = newState

        self.__hookNotifier(self.state, oldState)

    """
    Get current state of the app
    @memberOf Ragnarok
    @public
    @param {self} self This class
    @return {Dictionary} returns a copy of the current state to disable mutability
    """
    def getState (self):
        return self.state.copy()

    """
    Set a proxy of the state, when state is update this hook will be fire
    @memberOf Ragnarok
    @public
    @param {self} self This class
    @param {Function} fn Pass the hook method as parameter, this will be used as notifier
    """
    def setOnUpdateHook (self, fn):
        self.onUpdateHook = fn

    """
    Update state of the application
    @memberOf Ragnarok
    @private
    @param {self} self This class
    @param {Dictionary} newState Accepts the new state
    @param {Dictionary} oldState Save the previus state
    """
    def __hookNotifier (self, newState, oldState):
        if self.onUpdateHook is not None:
            self.onUpdateHook(newState, oldState)
        else:
            return None
