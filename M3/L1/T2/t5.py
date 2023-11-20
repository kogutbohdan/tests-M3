'''
Медіана - число, яке ділить ряд чисел на дві рівні частини, 
в одній з яких числа більше медіани, в іншій - менше. 
Давай напишемо програму, яка виводить медіану трьох чисел!

В основній програмі користувач вводить три числа, 
які передаються в якості параметрів в функцію. 
Функція повинна повернути медіану трьох чисел, 
тобто середнє з цих чисел. 
Наприклад, серед чисел 4, 6, 2 медіаною є число 4. 
Серед чисел 5 4 5 медіаною є 5.
'''

import math

def medianaNumbers(*numbers):
    numbers=list(numbers)
    numbers.sort()
    indexMediana=math.floor((len(numbers)-1)/2)
    return numbers[indexMediana]

a=int(input("number1:"))
b=int(input("number2:"))
c=int(input("number3:"))

result=medianaNumbers(a,b,c)

print(f"серед чисел {a}, {b}, {c} медіаною є число {result}")