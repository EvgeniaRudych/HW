from __future__ import annotations
from typing import Dict, Any
import random
from abc import abstractmethod
from typing import Dict, Any
from abc import ABC, ABCMeta
import uuid
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):

        if self.current_power == 0:
            forest.remove_animal(self)
        prey = random.choice(list(forest.animals.values()))
        if prey.id == self.id:
            print("Your predator was left without a dinner")
        else:
            if (self.speed > prey.speed) and (self.current_power > prey.current_power):
                print("Your predator has found its dinner")
                self.current_power = (self.current_power + self.current_power * 0.5)
            else:
                print("Predator hasn't eaten today.It is starving!")
                self.current_power = (self.current_power - self.current_power * 0.3)
                prey.current_power = (prey.current_power - prey.current_power * 0.3)

    def __str__(self):
        return f'{self.__class__.__name__}'


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def __str__(self):
        return f"{self.__class__.__name__}"

    def eat(self, forest: Forest):
        self.current_power = (self.current_power + self.current_power * 0.5)
        print("Herbivorous has eaten well")


AnyAnimal = [Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print("A new animal was added to the forest")
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print("An animal was removed from forest")
        self.animals.pop(animal.id)

    def any_predator_left(self, animal: AnyAnimal):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        new_animal = random.choice((Predator(random.randint(25, 100), random.randint(25, 100)),
                                    Herbivorous(random.randint(25, 100), random.randint(25, 100))))
        new_animal.id = uuid.uuid4()
        yield new_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(5):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        from time import sleep

        animal_to_remove = []
        for animal in forest.animals.values():
            if animal.current_power < 1:
                animal_to_remove.append(animal.id)
        for animal.id in animal_to_remove:
            forest.remove_animal(forest.animals[animal.id])
        if not forest.any_predator_left(animal):
            print("There are no predators in the forest anymore")
            break
        for animal in forest.animals.values():
            animal.eat(forest=forest)
        sleep(1)
