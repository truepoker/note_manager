collect_note = [{1:'Алексей', 2:'Список покупок', 3:'Купить продукты на неделю'}, {1:'Мария', 2:'Учеба', 3:'Подготовиться к экзамену'}]
print('Список всех заметок')
for n in range(len(collect_note)):
    print('Имя пользователя: ', collect_note[n][1])
    print('Заголовоки заметки: ', collect_note[n][2])
    print('Описание заметки: ', collect_note[n][3])
flag = True
while flag :
    word = input('Введите имя пользователя или заголовок для удаления заметки: ').lower()
    flag_k = False
    for note in collect_note :
        for i,j in note.items() :
            if (j.lower() == word) and (i != 3) :
                flag_k = True
                keys = input('Вы уверены, что хотите удалить заметку? (да/нет)').lower()
                while keys != 'нет':
                    if keys == 'да':
                        collect_note.remove(note)
                        print('Успешно удалено. Остались следующие заметки:')
                        break
                    else:
                        print('Введен не корректный ответ')
                        keys = input('Вы уверены, что хотите удалить заметку? (да/нет)').lower()
                if keys == 'нет':
                    print('Остались следующие заметки:')
    if flag_k != True :
        print('Заметок с таким именем пользователя или заголовком не найдено.')
        print('Остались следующие заметки:')
    flag = False
for n in range(len(collect_note)):
    print('Имя пользователя: ', collect_note[n][1])
    print('Заголовоки заметки: ', collect_note[n][2])
    print('Описание заметки: ', collect_note[n][3])

