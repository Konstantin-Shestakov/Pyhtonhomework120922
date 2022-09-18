import random


# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)
# ___________________________________________________________________________________________________________________________________________


# num = int(input("Сколько знаков после запятой, числа Пи "))
# PI = (1/16**0) * (4/(8 * 0 + 1) - 2/(8 * 0 +4) - 1/(8 * 0 + 5) - 1/(8 * 0 + 6))

# for k in range(1, num):
#    PI += (1/16**k) * (4/(8 * k + 1) - 2/(8 * k +4) - 1/(8 * k + 5) - 1/(8 * k + 6))

# print(round(PI, num))


# ___________________________________________________________________________________________________________________________________________
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# ___________________________________________________________________________________________________________________________________________



# num = 600
# num = int(input("Введите число, а я выведу его простые множители "))
# i = 2
# while i <= num: 
#     if num % i == 0:
#         print(i, end = " ")
#         num //= i
#         i = 1
#     i += 1




# ___________________________________________________________________________________________________________________________________________
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# ___________________________________________________________________________________________________________________________________________



# arr, new_arr = [random.randint(1,10) for i in range(10)], list()
# print(arr, '- заданная последовательность')
# for i in range(len(arr)):
#     if arr.count(arr[i]) == 1: new_arr.append(arr[i])
   
                                
# print(new_arr, '-список неповторяющихся элементов')

# ___________________________________________________________________________________________________________________________________________
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ___________________________________________________________________________________________________________________________________________


# k = int(input("Введите число: "))

# while k >= 0:
#      num = random.randint(0, 101)
#      if num == 0 and k == 0: print(" = 0")
#      elif num == 0:
#          k -= 1
#          continue
#      if k == 0: print(f"{num} = 0")
#      elif k == 1: print(f"{num}x + ", end = "")
#      else: print(f"{num}x**{k} + ", end = "")
#      k -= 1

# ___________________________________________________________________________________________________________________________________________
# 35. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# ___________________________________________________________________________________________________________________________________________


data = []
for f in range(1, 3):
    file_name = f'new{f}.txt'

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            data.append(line)


res = " + ".join(data)

# # СОЗДАНИЕ И ЗАПИСЬ В ФАЙЛ
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f'{res}')





# ________________________________________________________________________________________________________________________________________
# доп
# Дружественные числа
# Два различных натуральных числа называются дружественными, если первое из них равно сумме делителей второго числа,
# за исключением самого второго числа, а второе равно сумме делителей первого числа, за исключением самого первого числа.
# Требуется найти все пары дружественных чисел, оба из которых принадлежат промежутку от M до N.

# Входные данные

# В первой строке находятся целые числа M и N (1  ≤ M ≤ N ≤ 1 000 000).

# Выходные данные

# В каждой строке вывести по паре чисел через пробел. Первое число пары должно быть меньше второго.
# Строки должны быть отсортированы в порядке возрастания первого числа пары.
# Если пар дружественных чисел в промежутке нет, вывести "Absent".

def all_divider_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

def friend_num(lst):
    r = []
    for i in range(len(lst) - 1):
        M = lst[i]
        for j in range(i+1, len(lst)):
            K = lst[j]
            div_M = all_divider_sum(M)
            div_K = all_divider_sum(K)
            if div_M == K and div_K == M :
                r.append((div_M, div_K))
    return r

start = 200
end = 500

lst = [i for i in range(start,  end)]

result_lst = friend_num(lst)

if result_lst:
    for i in result_lst:
        print(min(i), max(i))
else:
    print('Absent')

# 220 284
# 1184 1210

























# ДИСКУСИЯ ВНЕ ДЗ
# ________________________________________________

# import math
# arr = [2, 7, 5, 8, 2, 4, 1]
# # arr = [int(i) for i in ''.split()]
# new_arr = list()
# j = -1

# for i in range(math.ceil(len(arr) / 2)):
#     new_arr.append(arr[i] * arr[j])
#     j -= 1

# print(new_arr)


# n = 10
# # num = int(input('Введите число:  '))

# def fibb(num):
#     lst = [0]
#     num_1 = 1
#     num_2 = 1
#     res = 0
#     for i in range(1, num + 1):
#         num_1 = num_2
#         num_2 = res
#         res = num_1 + num_2
#         print(res, end=' ')
#         lst.append(res)