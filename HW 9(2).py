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

# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0, кількість сміття більша ніж певне число
# опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
# можете придумати ще свої ексепшини і як їх опрацьовувати
import time


class Roomba:
    def __init__(self, charge, fullness, water_amount):
        self.charge = 100
        self.fullness = 0
        self.water_amount = 100

    def wash(self):
        if self.water_amount == 0:
            raise NoWater
        elif self.water_amount < 5:
            raise NotEnoughWater
        else:
            self.water_amount -= 5

    def vacuum_cleaner(self):
        if self.fullness == 100:
            raise NoRoom
        elif self.fullness > 90:
            raise NotEnoughRoom
        else:
            self.fullness += 10

    def charging(self):
        if self.charge == 0:
            raise NoCharge
        elif self.charge < 20:
            raise NotEnoughCharge
        else:
            self.charge -= 5

    def move(self):
        while True:
            print(f"moving")
            try:
                self.wash()
            except NoWater:
                print(f"No water.Can't wash")
            try:
                self.vacuum_cleaner()
            except NoRoom:
                print(f"No room. Can't clean anymore")
            try:
                self.charge()
            except NoCharge:
                print(f"No energy")
                break
            except NotEnoughCharge:
                print("Can't move!Need more energy")
                time.sleep(1)


