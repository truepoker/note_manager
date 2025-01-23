from datetime import datetime

d = datetime.today()
print(d.today())
print('Текущая дата: ', d.strftime('%d-%m-%Y'))
flag = True
while flag :
    try:
        issue_date = datetime.strptime(input('Введите дату дедлайна (в формате день-месяц-год): '),'%d-%m-%Y')
    except:
        print('Неверный формат ввода даты')
    else:
        flag = False
delta = d.date()-issue_date.date()
if delta.days>0 : print('Дедлайн истек ' + str(delta.days) + ' дня назад')
elif delta.days<0 : print('До дедлайн осталось ' + str(abs(delta.days)) + ' дня')
else : print('Дедлайн сегодня')

