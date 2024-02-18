"""Вывести четные числа от 2 до N по 5 в строку"""
N = int (input("Введите число"))
a = 0 # счётчик
for i in range (2, N, 2):
    a += 1
    if a == 5:
        print(i, end="\n")
        a = 0
    else:
        print(i, end=" ")
