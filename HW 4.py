# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f'Max speed is {self.max_speed} and mileage is {self.mileage}')


vehicle = Vehicle("60 km", "70 miles")
vehicle.print_vehicle()


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def capacity(self):
        print(f'Seating capacity is {self.seating_capacity}')

bus = Bus("50 km", "400 miles", "40 sits")
bus.print_vehicle()
bus.capacity()


# 3.Determine which class a given Bus object belongs to (Check type of an object)
my_bus = Bus("30 km", "20 miles", "40 sits")
print(type(my_bus))

# 4.Determine if School_bus is also an instance of the Vehicle class
your_bus = Bus("80 km", "56 miles", "21 sits")
print(isinstance(my_bus, Bus))


# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6 *.Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity):
        School.__init__(get_school_id, number_of_students)
        Bus.__init__(max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
class Bear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Roar')


class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        self.name = name
        self.age = age
        print('Woof')

bear = Bear("Umka", 2)
wolf = Wolf("Freki", 10)

for animal in (bear, wolf):
    animal.make_sound()


# 8.Create class City with name, population instance attributes, return a new instance only when population > 1500, otherwise return message: "Your city is too small".


class City:
    def __int__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    # 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
    def __str__(self):
        return 'The population of the city {self.name} is {self.population}'


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.
class Count:
    def __init__(self, count):

        self.count = count

    def __add__(self, other):
        if self.count or other.count > 10:
            total.count = self.count * self.other
        else:
            total.count = self.count + self.other
        return Count(total.count)


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class CallArea:
    def __call__(self, a, b):
        c = a + b
        return c


area = CallArea()
print(area(3, 4, ))


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
bool(order_1)
True
bool(order_2)
False
