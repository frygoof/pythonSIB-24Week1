# number = input("Введите число: ")
# string = input("Введите строку: ")
#
# print("Вы ввели число:", number)
# print("Вы ввели строку:", string)

# seconds = int(input("Введите время в секундах: "))
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# rem_seconds = seconds % 60
# time = "{:d}:{:02d}:{:02d}".format(hours, minutes, rem_seconds)
# print("Время в формате hour:min:sec:", time)

# n = input("Введите число n: ")
# nn = int(n * 2)
# nnn = int(n * 3)
# n = int(n)
# result = n + nn + nnn
# print(f"{n} + {nn} + {nnn} = {result}")

# number = int(input("Введите целое положительное число: "))
# max_digit = 0
# while number > 0:
#     digit = number % 10
#     if digit > max_digit:
#         max_digit = digit
#     number //= 10
# print("Самая большая цифра в числе:", max_digit)

# a = float(input("Введите начальный результат (a): "))
# b = float(input("Введите желаемый результат (b): "))
# day = 1
# while a < b:
#     print(f"{day}-й день: {a:.2f} км")
#     a *= 1.1
#     day += 1
# print(f"На {day}-й день спортсмен достиг результата — не менее {b} км.")

# revenue = float(input("Выручка: "))
# expenses = float(input("Избыток: "))
#
# profit = revenue - expenses
#
# if profit > 0:
#     print("Фирма работает с прибылью.")
#     profitability = profit / revenue * 100
#     print(f"Рентабельность: {profitability:.2f}%")
#     num_employees = int(input("Введите численность сотрудников фирмы: "))
#     profit_per_employee = profit / num_employees
#     print(f"Прибыль фирмы в расчёте на одного сотрудника: {profit_per_employee:.2f}")
# elif profit < 0:
#     print("Фирма работает с убытком.")
# else:
#     print("Фирма вышла в ноль.")