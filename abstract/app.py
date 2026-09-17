from abc import ABC, abstractmethod
from annotationlib import Format, get_annotations

from rich import print


class Animal(ABC):

  def __init__(self, name: str) -> None:
    self.name = name

  @abstractmethod
  def sound(self) -> None:
    ...

  @abstractmethod
  def move(self) -> None:
    ...


class Cat(Animal):

  def __init__(self, name: str) -> None:
    super().__init__(name)

  def sound(self) -> None:
    print("Meow")

  def move(self) -> None:
    print("The cat is walking gracefully.") 
  
cat = Cat("Whiskers")
print(cat.name)
cat.sound()
cat.move()

