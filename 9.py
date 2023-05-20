# Профилирование и отладка
# Мы с вами люди, а людям суждено ошибаться, даже при написании программного
# кода 🙂
# Давайте разберем с Вами самые частые ошибки в написании кода на Python.
# 🔥 Самые распространенные ошибки:
# ● SyntaxError(Синтаксическая ошибка)

# number_first = 5
# number_second = 7
# if number_first > number_second: # !!!!!
#     print(number_first)
# # Отсутствие :

# # ● IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
#     print(number_first) # !!!!!
# # Отсутствие отступов

# ● TypeError(Типовая ошибка)
# text = 'Python'
# number = '5' #испраивили добавив строку вместо 5 на '5'
# print(text + number)
# # Нельзя складывать строки и числа

# ● ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 1
# print(number_first // number_second)
# # Делить на 0 нельзя

# # ● KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[2])
# # Такого ключа не существует

# ● NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(name)
# # Переменной names не существует

# ● ValueError(Ошибка значения)
# text = '555'
# print(int(text))
# Нельзя символы перевести в целые значения

