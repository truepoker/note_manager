def create_note() :
    # подключение библиотеки для работы с даой и временем
    from datetime import datetime

    collect_note = []
        # добавление заметки
    username = input('Введите имя пользователя: ')
    flag_t = True
        # проверка корректности ввода заголовка заметки
    while flag_t:
        title = input('Введите заголовок заметки: ')
        if title == '':
            print('Загаловок заметки не может быть пустым')
        else:
            flag_t = False
    flag_c = True
        # проверка корректности ввода описания заметки
    while flag_c:
        content = input('Введите описание заметки: ')
        if content == '':
            print('Описание заметки не может быть пустым')
        else:
            flag_c = False
    status = input('Введите статус заметки (новая, в процессе, выполнено): ')
    created_date = datetime.now().strftime('%d-%m-%Y')
    print('Дата создания заметки: ', created_date)
    flag_id = True
    while flag_id:
            # проверка корректности ввода даты дедлайна заметки
        try:
            issue_date = datetime.strptime(input('Введите дедлайн (день-месяц-год): '), '%d-%m-%Y')
        except:
            print('Неверный формат ввода даты')
        else:
            flag_id = False
        # добавление заметки в список
    note = {1: username, 2: title, 3: content, 4: status, 5: created_date, 6: issue_date}
    collect_note.append(note)
    return collect_note
note = create_note()
for n in range(len(note)):
    print('Имя пользователя: ', note[n][1])
    print('Заголовоки заметки: ', note[n][2])
    print('Описание заметки: ', note[n][3])
    print('Статус заметки: ', note[n][4])
    print('Дата создания заметки: ', note[n][5])
    print('Дата истечения заметки (дедлайн): ', note[n][6].strftime('%d-%m-%Y'))