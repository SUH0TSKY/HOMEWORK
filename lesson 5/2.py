"""Сделать калькулятор: у пользователя
спрашивается число, потом действие и второе
число"""
number1 = input("Введите число 1 ")
sign = input("Введите знак: +, - , * , / ")
number2 = input("Введите число 2 ")

if sign == "+":
   number3 = number1 + number2
   print(number3)
elif sign == "-":
    number3 = number1 - number2
    print(number3)
elif sign == "*":
    number3 = number1 * number2
    print(number3)
elif sign == "/":
    number3 = number1 / number2
    print(number3)
else:
    print("Введите корректно знак или число")

