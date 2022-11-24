from model import get_info
from logger import writing_scv, read_contact, writing_txt

print('Выберите режим работы со справочником: ')
print('1. Записать нового абонента\n2. Вывести справочник на экран')
mode = int(input())
if mode == 1:
    a = get_info()
    writing_txt(a) 
    writing_scv(a)

elif mode == 2:
    print(read_contact())

else:
    print('Введено неверное значение!')