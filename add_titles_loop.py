#Интерактивный способ создания заголовков заметки
#создаем множество для определения завершения цикла создания заголовков
stop_while = {"" : 1, "стоп" : 2}
#инициализируем пустой список заголовков
title = []
#Записыаем заголовок или ключевое слово для завершения цикла в переменную keys
keys = input('Введите заголовок (или оставьте пустым или введите "стоп" для завершения): ')
#создаем цикл в котором проверяем входит ли keys в множество для завершения цикла,
#если да, то завершаем цикл выводим спиок заголовков, если нет просим ввести новый заголовок
while stop_while.get(keys.lower()) == None :
#проверяем входит ли заголовок в список заголовков, если да информируем, что заголовк уже существует
#если нет добавляем в список заголовков
    if keys in title : print('Введеный заголовок уже существует')
    else : title.append(keys.lower())
    keys = input('Введите заголовок (или оставьте пустым или введите "стоп" для завершения): ')
#выводим список заголовков с помощью цикла
print('Заголовки заметки:')
n = 0
for n in range(len(title)):
    print('-', title[n])
    n = +1
#
