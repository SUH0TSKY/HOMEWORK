""" список чисел и на вход поступает число N, необходимо сместить список на
указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]"""
from collections import deque

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (values)
N = int(input("Введите число N"))
values = deque(values)
values.rotate(N)
print(values)

