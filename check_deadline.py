#подключение библиотеки для работы с датой и временем
from datetime import datetime
#запись текущей даты
d = datetime.today()
print('Текущая дата: ', d.strftime('%d-%m-%Y'))
flag = True
while flag :
#проверка корректности ввода даты
    try:
        issue_date = datetime.strptime(input('Введите дату дедлайна (в формате день-месяц-год): '),'%d-%m-%Y')
    except:
        print('Неверный формат ввода даты')
    else:
        flag = False
#разница междутекущей датой и датой дедлайна
delta = d.date()-issue_date.date()
#проверка сколько дней осталось до дедлайна, или дата просрочена
if delta.days>0 : print('Дедлайн истек ' + str(delta.days) + ' дня назад')
elif delta.days<0 : print('До дедлайн осталось ' + str(abs(delta.days)) + ' дня')
else : print('Дедлайн сегодня')

