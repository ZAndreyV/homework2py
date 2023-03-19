# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input("Enter natural number: "))
# count = 0
# while 2 ** count < N:
#     x = 2 ** count
#     count += 1
#     print(x)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# s = int(input("enter natural number: "))
# p = int(input("enter natural number: "))
#
# for x in range(0, 1001):
#     for y in range(0, 1001):
#         if x + y == s and x * y == p:
#             print(x, y)
#

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("enter amount of coins: "))
# list1 = []
# for i in range(n):
#     i = list1.append(int(input(f"Enter mean of coin {i}:")))
# count_tails = 0
# count_eagle = 0
# for i in list1:
#     if i == 0:
#         count_tails += 1
#     elif i == 1:
#         count_eagle += 1
# if count_tails < count_eagle:
#     print(count_tails)
# else:
#     print(count_eagle)