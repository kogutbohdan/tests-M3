'''
Давай допоможемо фізикам перевести час в секунди!

Коли вчені-фізики виконують експеримент, 
витрачений на нього час вимірюється в секундах, 
навіть якщо досвід тривав більше декількох годин. 
Давай полегшимо життя фізикам і напишемо програму, 
яка буде переводити витрачені години та хвилини в секунди.

Користувач вводить два числа: 
h - кількість годин і m - кількість хвилин.

Підключи модуль my_time з попереднього завдання,
використовуй функції переведення часу в секунди.

Виведи витрачений час в секундах.
'''
from my_time import*
# Підключи модуль з попереднього завдання

h = int(input("Введи кількість годин: "))
m = int(input("Введи кількість хвилин: "))
print("секунди:{sec}".format(sec=seconds_in_min(m)+seconds_in_hour(h)))
