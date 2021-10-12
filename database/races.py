"""Race object"""

from typing import Protocol
from dataclasses import dataclass
import random as rn

class Race(Protocol):
    """Basic propierties"""
    #name
    name: str
    #size is a str, accetable values are Small, Medium or Big
    size: str
    #speed is an int, random selected in a range of numbers between 1 and 10
    speed: int
    #QI is an int, random selected in a range of numbers between 0 and 100
    QI: int
    
    def print_properties(self) -> None:
        """Print properties"""

@dataclass
class Shepard(object):
    name: str = "Shepard"
    size: str = "Big"
    speed: int = rn.randint(2,4,1)
    QI: int = rn.randint(20,40,1)
    
    def print_properties(self) -> None:
        print (f'size: {self.size}')
        print (f'speed: {self.speed}')
        print (f'QI: {self.QI}')
        
@dataclass
class German_Shepard(object):
    name: str = "German Shepard"
    size: str = "Big"
    speed: int = rn.randint(3,6,1)
    QI: int = rn.randint(40,75,1)
    
    def print_properties(self) -> None:
        print (f'size: {self.size}')
        print (f'speed: {self.speed}')
        print (f'QI: {self.QI}')
