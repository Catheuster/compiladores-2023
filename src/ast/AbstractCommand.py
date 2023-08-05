from abc import ABC, abstractmethod

class AbstractCommand:
    def __init__(self):

        @abstractmethod
        def generateJavaCode(self):
            pass

        @abstractmethod
        def generatePythonCode(self):
            pass

        @abstractmethod
        def generateJavaScriptCode(self):
            pass