import dataclasses
import collections


# 1.
class Laptop:
    def __init__(self, battery, brand):
        self.battery = Battery
        self.brand = brand

    """
    Make the class with composition.
    """


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    """
    Make the class with composition.
    """


laptop = Laptop("nickel", "Xiomi")
print(laptop)


# 2.
class Guitar:
    def __init__(self, strings, type):
        self.strings = GuitarString
        self.type = type

    """
    Make the class with aggregation
    """


class GuitarString:
    def __init__(self, material):
        self.material = material

    """
    Make the class with aggregation
    """


guitarstrings = GuitarString('nylon')
guitar = Guitar(guitarstrings, 'ukulele')


# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """

    @staticmethod
    def __add_nums__(a, b, c):
        return a + b + c


print(Calc.__add_nums__(3, 4, 5))


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, list):
        self.list = list

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


# 5 *.

class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

        @property
        def visitors_count(self):
            return self.visitors_count

        @visitors_count.setter
        def visitors_count(self, visitors_count):
            if visitors_count > self.max_visitors_num:
                self.visitors_count = max_visitors_num
            else:
             self.visitors_count = self.visitors_count






Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)  # 50


# 6.
@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7. Create the same class (6) but using NamedTuple

AddressBookDataClass = collections.namedtuple('AdressBookDataClass',
                                              ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

8.


class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

        def __str__(self):
            return f"(key: {self.key}, name: {self.name}, phone_number: {self.phone_number}, address: {self.address}, email: {self.email}, birthday: {self.birthday}, age: {self.age})"

    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """


# 9.
class Person:
    name = "John"
    age = 36
    country = "USA"
    """
    Change the value of the age property of the person object
    """


john = Person()

setattr(john, "age", 12)

print(getattr(john, 'age'))


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(123456, 'Mark')
setattr(student, 'student_email', 'mark@ukma.edu.ua')
print(getattr(student, 'student_email'))


# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

        @property
        def fahrengheit(self):
            return ((temperature * 1.8) + 32)


# create an object
my_temperature = Celsius(40)
print(my_temperature._temperature)
