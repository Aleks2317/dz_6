"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
 На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
 является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от
результата проверки.

Пример использования На входе:


date_to_prove = 15.4.2023
На выходе:


True

"""


# __MONTHS = {
#     1: range(1, 32),
#     2: range(1, 29),
#     3: range(1, 32),
#     4: range(1, 31),
#     5: range(1, 32),
#     6: range(1, 31),
#     7: range(1, 32),
#     8: range(1, 32),
#     9: range(1, 31),
#     10: range(1, 32),
#     11: range(1, 31),
#     12: range(1, 32),
# }
#
#
#
# def parse_data(date: str) -> bool:
#     d, m, y = map(int, date.split('.'))
#     return _y_is_valid(y) and _m_is_valid(m) and _d_is_valid(d, m, y)
#
#
# def _d_is_valid(d: int, m: int, y: int) -> bool:
#     if _is_leap_year(y) and m == 2:
#         return d in range(1, 30)
#     return d in __MONTHS[m]
#
#
# def _m_is_valid(m: int) -> bool:
#     return m in range(1, 13)
#
#
# def _y_is_valid(y: int) -> bool:
#     return y in range(1, 10_000)
#
#
# def _is_leap_year(y: int) -> bool:
#     return y % 4 == 0 and y % 100 != 0 or y % 400 == 0
#
#
# date_to_prove = '15.4.2023'

# print(parse_data(date_to_prove))



# аналогичное решение
# date_to_prove = '29.2.2024'
#
# from datetime import date
#
# def data_test(dat: str) -> bool:
#     d, m, y = map(int, dat.split('.'))
#     try:
#         date(y, m, d)
#     except ValueError:
#         return False
#     return True
#
# print(data_test(date_to_prove))


'''
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, 
в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на 
одной вертикали, горизонтали или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.

Пример использования На входе:


print(generate_boards())
На выходе:


[[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]

'''

# from random import randint
#
# def generator_numb():
#     x, y = randint(1, 8), randint(1, 8)
#     return x, y
#
# def generate_boards():
#     board_list = []
#     while len(board_list) != 4:
#         list_f = [generator_numb()]
#         while len(list_f) != 8:
#             x, y = generator_numb()
#             poz = (x, y)
#             j = True
#             if poz not in list_f:
#                 for i in list_f:
#                     if poz[0] == i[0] or poz[1] == i[1] and poz[0] != poz[1]:
#                         j = False
#                     if abs(poz[0] - i[0]) == abs(poz[1] - i[1]) and poz[0] != poz[1]:
#                         j = False
#                 if j == True:
#                     list_f.append((x, y))
#         if list_f not in board_list:
#             board_list.append(list_f)
#     return board_list
#
#
# g = generate_boards()
# print(g, len(g), sep='\n')
#
#
""" # решение рекомендуемое"""
#
# import random
# from itertools import combinations
#
# def generate_board():
#     # Генерируем случайную доску
#     board = []
#
#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board
#
# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True
#
# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list


