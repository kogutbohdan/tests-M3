'''
Етап «Правила гри»
Використовуй команду print (), щоб привітатися з гравцем і пояснити йому правила гри.

Етап «Питання-відповідь»: генерація задуманого числа
Нехай програма загадає число. Для цього підключи модуль random і використовуй команду randint (a, b), де a і b - межі, в яких потрібно видати випадкове число.

Етап «Питання-відповідь»: введення числа користувачем
Запроси у користувача його варіант відповіді за допомогою команди input ().

Етап «Питання-відповідь»: підказки
Порівняй за допомогою умовного оператора введене користувачем число з задуманим. Якщо вони не збігаються, виведи підказку, більше загадане число або менше введеного варіанти відповіді.

Етап «Питання-відповідь»: повтор введення
Додай в програму цикл, щоб користувач міг повторно вводити варіант відповіді, поки не відгадає.

Етап «Результат гри»
Привітай користувача з перемогою і виведи на екран загадане число.

Бонус: додай в програму підрахунок спроб!
'''

from random import randint

counter=0

userName=input("Введіть своє імя:")
start=randint(-1000,100)
end=randint(200,1000)

print(f"Пивіт {userName}")
print(f"Я загадую число від {start} до {end} ви маєте його відгадати")

randomNumber=randint(start,end)

number=-1001

while number!=randomNumber:
    number=int(input("Введіть число:"))
    counter+=1
    if(number==randomNumber):
        print(f"вітаю ви вгадали {userName}")
        print(f"загадане число {randomNumber}")
        print(f"кількість спроб {counter}")
    elif(number>randomNumber):
        print("шукане число менше")
    elif (number<randomNumber):
        print("шукане число більше")
