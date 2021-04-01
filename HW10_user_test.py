# Task3
# Напишіть тести до модуля реєстрації юзера (без фласк АРІ, просто окремий клас)
#1) тести повинні перевіряти чи відповідає пароль, пошта і ім'я вимогам,
# 2)перевіряти чи юзера з таким іменем не має в базі
# 3)якщо юзер створений то назад отримуємо строку "200",
# 4)інакше модуль реєстрації кидатиме ексепшини (ексепшини потрібно написати свої)

# тести до модуля авторизації юзера
# метод авторизації отримує пошту і пароль і звіряє чи є такі в базі данних (за бд можете використати словник)
# якщо дані введені вірно, і юзер існує, то назад повертаєтсья обєкт класу UserToken (майже пустий клас,
# містить тільки аргумент строку яка задається рандомним набором символів)
# Після написання тестів, реалізуйте ваші методи реєстрації і авторизаії

import unittest


class TestRegistration(unittest.TestCase):
    def setUpClass(cls) -> None:
        self.test_registration = Registration()

    def test_autorisation(self):
        email = evgeniar2804@gmail.com
        name = Evgenia
        password = evgeniaevgenia
        self.assertEqual(self.test_registration.autoridation(email, name, password), 200)

    def test_len(self):
        #Your name should include more than 3 symbols and less than 25
        email = evgeniar2804 @ gmail.com
        name = Evg
        password = evgeniaevgenia
        with self.assertRaises(NameLenError):







