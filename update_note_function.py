#note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}


def update_note(note) :
    from datetime import datetime

    keys = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ').lower()
    flag = True
    while flag :
        if keys in note :
            if keys == 'issue_date' :
                print('Текущее значение для ' + keys + ' : ' + note[keys])
                flag_id = True
                while flag_id:
                    # проверка корректности ввода даты дедлайна заметки
                    try:
                        note[keys] = datetime.strptime(input('Введите дедлайн (день-месяц-год): '), '%d-%m-%Y').strftime('%d-%m-%Y')
                    except:
                        print('Неверный формат ввода даты')
                    else:
                        flag_id = False
                        flag = False
            else :
                print('Текущее значение для ' + keys + ' : ' + note[keys])
                note[keys] = input('Введите новое значение для ' + keys + ' : ')
                flag = False
        else :
            print('Таких данных нет')
            keys = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ').lower()
note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
update_note(note)
print(note)