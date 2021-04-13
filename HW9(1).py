# Task 1
# Напишіть калькулятор в якого будуть реалізовані операції додавання,
# віднімання, множення, ділення, піднесення в степінь,
# взяття з під кореня, пошук відсотку від числа

# Огорніть в конструкцію try... except... потенційно "небезпечні" місця,
# наприклад отримання числа і приведення до типу даних
# або інструкції математичних операцій

# заповніть ваш скрипт логами
# Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
# + логи з помилками
# причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
# лог файл завжди відкриваєтсья в режимі дозапису.
# так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки
import logging

log_template = ' %(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='HW9_1.log', filemode='a', format=log_template)

logging.info(f"This is a calculator")


def sum_operation():
    print(f"sum")
    logging.info("This is a sum operation")
    str_x = input("Enter your first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error(" X is not a number!")
        return
    str_y = input(" Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number!")
        return
    z = x + y
    print(f"{x} + {y} = {z}")
    logging.info("You got your sum")
    return z


def subtract_operation():
    print(f"subtraction")
    logging.info("This is a subtraction operation")
    str_x = input(" Enter yout first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error("X is not a number!")
        return
    str_y = input("Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number")
        return
    z = x - y
    print(f"{x} - {y} = {z}")
    logging.info("You got your subtraction")
    return z


def mult_operation():
    print(f"multiplication")
    logging.info("This is a multiplication operation")
    str_x = input(" Enter yout first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error("X is not a number!")
        return
    str_y = input("Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number")
        return
    z = x * y
    print(f"{x} * {y} = {z}")
    logging.info("You got your multiplication")
    return z


def div_operation():
    print(f"division")
    logging.info("This is a division operation")
    str_x = input(" Enter yout first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error("X is not a number!")
        return
    str_y = input("Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number")
        return
    try:
        z = x / y
        print(f"{x} / {y} = {z}")
        return z
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return


def exc_operation():
    print(f"exponentiation")
    logging.info("This is an exponentiation operation")
    str_x = input(" Enter yout first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error("X is not a number!")
        return
    str_y = input("Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number")
        return
    try:
        z = x ** y
    except ZeroDivisionError:
        print("You can't raise zero by negative power")
        logging.info("You can't raise a o by negative power")
        return
    return z


def sqrt_operation():
    print(f"square root")
    logging.info("This is an exponentiation operation")
    str_x = input(" Enter yout first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error("X is not a number!")
        return
    str_y = input("Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number")
        return
    try:
        z = x ** (1 / y)
        print(f"{x} ** (1 / {y}) = {z}")
        return z
    except ZeroDivisionError:
        print("You can't divide by zero")
        return


def percent_operation():
    print(f"square root")
    logging.info("This is an exponentiation operation")
    str_x = input(" Enter yout first number: ")
    try:
        x = float(str_x)
    except ValueError:
        logging.error("X is not a number!")
        return
    str_y = input("Enter your second number: ")
    try:
        y = float(str_y)
    except ValueError:
        logging.error("Y is not a number")
        return
    z = x / 100 * y
    print(f"{x} /(100 * {y}) = {z}")
    return z


sum_operation()
subtract_operation()
mult_operation()
div_operation()
exc_operation()
sqrt_operation()
percent_operation()
