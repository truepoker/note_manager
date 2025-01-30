collect_note = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
 {'username': 'Мария', 'title': 'Учеба', 'content': 'Сдать экзамен', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}]
#collect_note = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}]
#collect_note = []
def display_notes(notes) :
    name = ['Имя пользователя: ', 'Заголовок: ', 'Описание: ', 'Статус: ', 'Дата создания: ', 'Дедлайн: ']
    if len(notes) != 0 :
        # Вывод всех заметок
        for n in range(len(notes)) :
            print('Заметка №', n+1)
            g = 0
            for i,j in notes[n].items() :
                print(name[g], notes[n][i])
                g += 1
            print('--------------------------------')
    else :
        print('Копировать код')
        print('У вас нет сохранённых заметок.')
display_notes(collect_note)