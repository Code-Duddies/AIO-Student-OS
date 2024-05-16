from abc import ABC, abstractmethod

#Abstract parent of all tool classes
class AbstractTool(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def __del__(self):
        pass