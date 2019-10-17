from .src.Color import Color
from .src.LoggerTypes import LoggerTypes

class Logger:
    
    def __init__(self, level = 1):
        '''
        LEVEL : Type of log the logger will print to console
            
            ERROR = 3
            WARNING = 2
            INFO = 1
            NONE = 0
        '''
        self.level = level
        self.setLevel(level)

    def setLevel(self, level):
        '''
        Sets Level of output.

            ERROR = 3
            WARNING = 2
            INFO = 1
            NONE = 0
        '''
        for types in LoggerTypes:
            if types == level:
                self.level = types.value

    def Error(self, text):
        if self.level <= LoggerTypes.ERROR.value:
            self._write(Color.RED, text)

    def Warn(self, text):
        if self.level <= LoggerTypes.WARN.value:
            self._write(Color.YELLOW, text)

    def Info(self, text):
        if self.level <= LoggerTypes.INFO.value:
            self._write(Color.NONE, text)

    def _write(self, color="", text="", reset=True):
        out = color + str(text)
        if reset:
            out += Color.RESET
        print(out)
