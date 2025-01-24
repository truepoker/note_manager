from datetime import datetime

print('"Менеджер заметок"! Вы можете добавить новую заметку.')
flag = True
collect_note = []
while flag :
    username = input('Введите имя пользователя: ')
    flag_t = True
    while flag_t:
        title = input('Введите заголовок заметки: ')
        if title == '': print('Загаловок заметки не может быть пустым')
        else: flag_t = False
    flag_c = True
    while flag_c:
        content = input('Введите описание заметки: ')
        if content == '':
            print('Описание заметки не может быть пустым')
        else:
            flag_c = False
    status = input('Введите статус заметки (новая, в процессе, выполнено): ')
    flag_cd = True
    while flag_cd :
        try:
            created_date = datetime.strptime(input('Введите дату создания (день-месяц-год): '), '%d-%m-%Y')
        except:
            print('Неверный формат ввода даты')
        else:
            flag_cd = False
    flag_id = True
    while flag_id :
        try:
            issue_date = datetime.strptime(input('Введите дедлайн (день-месяц-год): '), '%d-%m-%Y')
        except:
            print('Неверный формат ввода даты')
        else:
            flag_id = False
    note = {1:username, 2:title, 3:content, 4:status, 5:created_date, 6:issue_date}
    collect_note.append(note)
    keys = input('Хотите добавить ещё одну заметку? (да/нет)').lower()
    while keys != 'нет':
        if keys == 'да':
            flag = True
            break
        else:
            print('Введен не корректный ответ')
            keys = input('Хотите добавить ещё одну заметку? (да/нет)').lower()
    if keys == 'нет':
        print('нет')
        flag = False
n = 0
for n in range(len(collect_note)):
    print('Имя пользователя: ', collect_note[n][1])
    print('Заголовоки заметки: ', collect_note[n][2])
    print('Описание заметки: ', collect_note[n][3])
    print('Статус заметки: ', collect_note[n][4])
    print('Дата создания заметки: ', collect_note[n][5].strftime('%d-%m-%Y'))
    print('Дата истечения заметки (дедлайн): ', collect_note[n][6].strftime('%d-%m-%Y'))
    n = +1