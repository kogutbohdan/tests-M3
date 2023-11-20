'''
Напишіть функцію
Програма просить ввести число n і друкує всі числа від n до 1 включно
'''

def inputNumber(number):
    step=1 if number<1 else -1
    for i in range(number,1,step):
        print(i)

inputNumber(100)