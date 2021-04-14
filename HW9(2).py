# Task 2
# Напишіть клас робота пилососа
# в ініт приймається заряд батареї, заповненість сміттєбака і кількість води

# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
# (в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
# також на кожній ітерації прінтиться "move"
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
# а кількість сміття збільшується

# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%,
# кількість води - 0, кількість сміття більша ніж певне число
# опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20%
# то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
# можете придумати ще свої ексепшини і як їх опрацьовувати
import time


class NoWater(Exception):
    pass


class NotEnoughWater(Exception):
    pass


class NoRoom(Exception):
    pass


class NotEnoughRoom(Exception):
    pass


class NoCharge(Exception):
    pass


class NotEnoughCharge(Exception):
    pass


class Roomba:
    water_intake = 5
    charge_intake = 5

    def __init__(self, charge, fullness, water_amount):
        self.charge = charge
        self.fullness = fullness
        self.water_amount = water_amount

    def wash(self):
        if self.water_amount == 0:
            raise NoWater
        elif self.water_amount < 5:
            raise NotEnoughWater
        else:
            self.water_amount = self.water_amount - self.water_intake

    def vacuum_cleaner(self):
        if self.charge > 20:
            self.charge -= self.charge_intake
        elif 1 < self.charge < 20:
            self.charge -= 1
            raise NotEnoughCharge
        else:
            raise NoCharge
        if self.fullness == 100:
            raise NoRoom
        elif self.fullness > 90:
            raise NotEnoughRoom
        else:
            self.fullness += 10


def wash(roomba):
    print("Washing")
    roomba.wash()


def vacuum_cleaner(roomba):
    print("Cleaning")
    roomba.vacuum_cleaner()


roomba1 = Roomba(33, 0, 33)


def move(roomba):
    i = 10
    while True:
        print("moving")
        try:
            wash(roomba)
        except NoWater:
                print("No water.Can't wash")
        except NotEnoughWater:
                print("Not enough water to continue")
        try:
            vacuum_cleaner(roomba)
        except NoRoom:
            print("No room. Can't clean anymore")
        except NoCharge:
            print("Not enough power")
            break
        except NotEnoughCharge:
            if i == 0:
                print("Can't move anymore")
                break
            else:
                i = i - 1
        time.sleep(1)


move(roomba1)
