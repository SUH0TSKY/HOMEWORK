"""Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы остались только строки, использование дополнительного списка
незаконно """

objs = [1, 2, 3, 4, "Hello", 5, 6, 7, "World", "!"]
list(filter(lambda x: x != int, objs))
print(objs)
