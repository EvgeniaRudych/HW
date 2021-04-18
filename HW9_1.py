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
    print("sum")
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
    print("subtraction")
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
    print("multiplication")
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
    print("division")
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
    print("exponentiation")
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


def root_operation():
    print("square root")
    logging.info("This is an root operation")
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
    print("percent operation")
    logging.info("This is an exponentiation operation")
    str_x = input(" Enter your first number: ")
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


while True:
    print("1. sum_operation")
    print("2. subtract_operation")
    print("3. mult_operation")
    print("4. div_operation")
    print("5. exc_operation")
    print("6. root_operation")
    print("7. percent_operation")
    print("0. quite")
    cmd = input("Choose a number you need: ")

    if cmd == "1":
        sum_operation()
    elif cmd == "2":
        subtract_operation()
    elif cmd == "3":
        mult_operation()
    elif cmd == "4":
        div_operation()
    elif cmd == "5":
        exc_operation()
    elif cmd == "6":
        root_operation()
    elif cmd == "7":
        percent_operation()
    elif cmd == "0":
        break
    else:
        print("Chosen number does not exist!")
