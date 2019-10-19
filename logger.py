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

        self.setLevel(level)

        self._errorColor = Color.RED
        self._warnColor = Color.YELLOW
        self._infoColor = Color.NONE


    def setLevel(self, level):
        '''
        Sets Level of output.

            ERROR = 3
            WARNING = 2
            INFO = 1
            NONE = 0
        '''
        if not (0 <= level <= 3):
            raise ValueError("Level must be an integer between 0 and 3")
        
        for types in LoggerTypes:
            if types.value == level:
                self.level = types.value
                break

    def Error(self, text):
        if self.level <= LoggerTypes.ERROR.value:
            self._write(self._errorColor, text)

    def Warn(self, text):
        if self.level <= LoggerTypes.WARN.value:
            self._write(self._warnColor, text)

    def Info(self, text):
        if self.level <= LoggerTypes.INFO.value:
            self._write(self._infoColor, text)

    def _write(self, color="", text="", reset=True):
        out = color + str(text)
        if reset:
            out += Color.RESET
        print(out)
