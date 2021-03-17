# Survival
#
# 1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
# Each animal is born with the following parameters (by using random):
# - strength (from 25 to 100 points)
# - speed (from 25 to 100 points)
# The force cannot be greater than it was at birth (initialization).
#
# At each step of the game we take 1 animal from the forest (iteration):
# - If it is herbivorous, then it eats (restores its strength by 50%).
# - If it is a predator, it hunts - randomly chooses an animal from the forest and:
#     - pulled himself out, he was unlucky and he was left without a dinner;
#     - pulled out another animal, then tries to catch up;
#     - if he can catch up, he catches up and attacks;
#     - if attacked and is stronger, then eats and restores 50% of strength;
#     - did not catch up or did not have enough strength, then he and the lucky prey lose 30% of strength (Because both either ran, or fought, or all together)
#
# An animal whose power has expired dies. (You can check the strength at the time of food search)
#
# The game continues as long as predators are present in the forest.


from __future__ import annotations

import random
from abc import abstractmethod
from typing import Dict, Any

import uuid
import time


class Animal:
    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal)
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)

    self.id = None
    self.max_power = power
    self.current_power = power
    self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        if self.current_power == 0:
            forest.remove_animal(self)
        prey = random.choice(len(forest.animals.values()))
        if prey.id == self.id:
            print(f"Your predator was left without a dinner")
        else:
            if self.speed > prey.speed and self.current_power > prey.current_power:
                print(f"Your predator has found its dinner")
                self.current_power = (self.current_power + self.current_power * 0.5)
            else:
                print(f"Predator hasn't eaten today.It is starving!")
                self.current_power = (self.current_power - self.current_power * 0.3)
                prey.current_power = (prey.current_power - prey.current_power * 0.3)


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        self.current_power = (self.current_power + self.current_power * 0.5)
        print(f"Herbivorous has eaten well")


AnyAnimal = Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print(f"A new animal was added to the forest")
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print("An animal was removed from forest")
        self.animals.pop(animal)


def animal_generator():
    while True:


new_animal = random.choice(Predator(random.randint(25, 100), random.randint(25, 100)),
                           Herbivorous(random.randint(25, 100), random.randint(25, 100)))
new_animal.id = uuid.uuid4()
yield new_animal

if __name__ == "__main__":
    nature = animal_generator()
    Forest = forest
    for i in range(10):
        animal = next(nature)
    forest.add_animal()
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    while True:
        if not forest.any_predator_left:
            print("There are no predators in the forest anymore")
            break
            for animal in forest:
                animal.eat(forest=forest)
                time.sleep(1)
