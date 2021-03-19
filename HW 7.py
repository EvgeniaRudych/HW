import pickle
import openpyxl

# Task 1
# У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст складається з  міток часу і репліки яка була сказана в той момент часу.
# Причому репліка знаходиться в наступному рядку після мітки часу.
# Результатом виконнання завдання повинно бути:
# 1. словник елементами якого буде пара ключ:значення де ключ - мітка часу, значення - репліка в даний момент часу
# 2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі субтитри повинні мати вигляд простого тексту.
# Це означає що окрім видалення міток часу, вам потрібно видалити переноси рядків

dict_1 = {}
file = open("task1.txt", "r")
content = file.readlines()
file.close()
for i in range(0, (len(dict_1)), 2):
    content[i] = content[i].replace("\n", "")
    content[i + 1] = content[i + 1].replace("\n", "")
    dict_1.update({content[i]: content[i + 1]})
print(dict_1)

with open("task1.txt", "w") as file:
    for item in dict_1.values():
        file.write(f"{item}")
# Task 2
# в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і знайдіть середнє арифметичне чисел що знаходяться в списку

file = open("task2", "rb")
task2_new = file.read()
task2_2 = pickle.load(task2_new)
file.close
mean_arith = (sum(task2_2) / len(task2_2))
print(mean_arith)


# Task 3
# Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку), напишіть контекстний менеджер для роботи з ексель.
# Даний менеджер повинен бути аналогом методу open()


class Workbook(object):
    def __init__(self, workbook_name):
        self.file_obj = openpyxl.load_workbook(workbook_name)

    def __enter__(self):
            return self.file_obj

    def __exit__(self, exc_type, exc_value, exc_traceback):
            self.file_obj.close()
