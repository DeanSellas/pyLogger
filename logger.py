import os

from datetime import datetime as dt
from .src.Color import Color
from .src.LoggerTypes import LoggerTypes

class Logger:
    
    def __init__(self, level = 1, filePath=""):
        '''
        LEVEL : Type of log the logger will print to console
            
            ERROR = 3
            WARNING = 2
            INFO = 1
            NONE = 0
        '''
        self.toFile = False
        self._LogTime = dt.now().strftime('%m%d%y')
        self.fileName = "{}_{}.txt".format("log", self._LogTime)        
        
        self.setLevel(level)

        self._errorColor = Color.RED
        self._warnColor = Color.YELLOW
        self._infoColor = Color.NONE
        self._inputColor = Color.BLUE

        self.setPath(filePath)

    def _fileChecks(self):
        if self.filePath == "" or self.filePath == None:
            return False
            
        if(not os.path.isdir(self.filePath)):
            r = self.Input("{} Does Not Exist Would You Like To Create It? [Y/n]".format(self.filePath))
            if r.lower() == 'n':
                self.Warn("{} Does Not Exist!".format(self.filePath))
                return False
            os.mkdir(self.filePath)
        return True

    def setLevel(self, level):
        '''
        Sets Level of output.

            ERROR = 3
            WARNING = 2
            INFO = 1
            NONE = 0
        '''
        if not (0 <= level <= 3):
            self.Error("Level must be an integer between 0 and 3", ValueError)
        
        for types in LoggerTypes:
            if types.value == level:
                self.level = types.value
                break
    
    def setPath(self, newPath):
        self.filePath = newPath
        self.toFile = self._fileChecks()

    def Error(self, text, ErrorType=None):
        if self.level <= LoggerTypes.ERROR.value:
            self._write(self._errorColor, "ERROR | {}".format(text))

        if ErrorType != None:
            raise ErrorType(text)

    def Warn(self, text):
        if self.level <= LoggerTypes.WARN.value:
            self._write(self._warnColor, "WARNING | {}".format(text))

    def Info(self, text):
        if self.level <= LoggerTypes.INFO.value:
            self._write(self._infoColor, "INFO | {}".format(text))

    def Input(self, text):
        print(self._inputColor)
        inp = input(text)
        out = "INPUT | {} {}".format(text, inp)
        self._write(self._inputColor, out, toConsole=False)
        return inp

    def Clear(self):
        self.Info("Console Cleared")
        os.system('cls')

    def _write(self, color="", text="", reset=True, toConsole=True):
        out = color + str(text)
        
        if toConsole:
            print(out)

        if self.toFile:
            with open(os.path.join(self.filePath,self.fileName), 'a', encoding='utf-8') as logFile:
                logFile.write(text+'\n')

        if reset:
            print(Color.RESET, end="")

    def csvWriter(self, fields, data):
        import csv
        with open(os.path.join(self.filePath, "output_{}.csv".format(self._LogTime)), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(data)