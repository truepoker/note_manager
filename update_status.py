# обновление статуса заметки
status = 'Не выполнено'
yes_no = {'да' : 1, 'нет' : 2}
start = True
while start == True :
    keys = input('Введите "да", если статус заметки изменеился на "выполнено", "нет"'
                 ' если статус заметки "не выполнено": ')
    if (yes_no.get(keys.lower()) == 1) :
        status = 'выполнено'
        start = False
    elif (yes_no.get(keys.lower()) == 2) :
        status = 'не выполнено'
        start = False
    else : print('не корректный ввод, введите "да" или "нет"')
print('Статус заметки: ',status)