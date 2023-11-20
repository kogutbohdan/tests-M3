'''
Нумо, переверни! Покажи свою майстерність кодингу!
Користувач вводить чотиризначне число. 
Виведи число, складене з тих самих цифр, 
записаних в зворотному порядку.
Рішення оформи у вигляді функції reverse (n), 
яка отримує на вхід введене користувачем число 
і повертає його перевертень.
'''
from M3.compose import compose


def reversNumber(number:int):
    strNum=str(number)
    resultNumber=""
    for i in range(-1,-(len(strNum)+1),-1):
        resultNumber+=strNum[i]
    resultNumber=int(resultNumber)
    return resultNumber

reversInputNumber=compose(print,reversNumber,int,input)
reversInputNumber("number1:")