from dataclasses import dataclass
from .races import Race

@dataclass
class Dog(Race):
    name: str
    owner: str
    hair: str
    hair_color: str
    eye_color: str

    def print_dog(self) -> None:
        print(f'{self.name} is a beautiful {Race.name} with {self.hair_color} {self.hair} hair and {self.eye_color} eyes.')

def dog_recall() -> Dog:
    return Dog
