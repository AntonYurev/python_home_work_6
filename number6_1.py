# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) 
# и дополнить нулём до двух целочисленных разрядов:
# spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# for i in range(len(spisok)):
#     if "+" in spisok[i] or "-" in spisok[i]:
#         if len(spisok[i]) == 2:
#             spisok[i]=spisok[i][:1]+"0"+spisok[i][1:]
#         spisok[i]='"'+spisok[i]+'"'
#     elif spisok[i].isdigit():
#         if len(spisok[i]) == 1:
#             spisok[i]="0"+spisok[i]
#         spisok[i]='"'+spisok[i]+'"'
# print(" ".join(spisok))


# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 
# Можно ли при этом не создавать новый список?
# def privet(spisok1):
#     for i in spisok1:
#         print(f'Привет {i.split()[-1]} !')

# spisok = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for i in range(len(spisok)):
#     s = spisok[i].split()[-1]
#     s = s[:1].upper() + s[1:].lower()
#     spisok[i]=spisok[i][:len(spisok[i])-len(s)]+s
# privet(spisok)
# print(spisok)


# Задание №5
# Создаем список, содержащий цены на товары (10–20 товаров)
import random
spisok_price = []
for i in range(10):
    spisok_price.append(round(random.random()*random.randint(1,100),2))
print('Наш список: ',spisok_price)
print()
def vivod(spisok):
    for i in range(len(spisok)):
        p=str(spisok[i])
        if len(p.split('.')[0]) == 1:
            p="0"+p
            spisok[i]=p      
        if len(p.split('.')[1]) == 1:
            p=p+"0"
            spisok[i]=p
        spisok[i]=p.replace('.',' руб ')+" коп"
    print('Наш список с рублями и копейками: ',', '.join(spisok))

vivod(spisok_price)
print()
print("Сортирорвка по возрастанию цен: ", ', '.join(sorted(spisok_price)))
print()
print("Сортировка по убыванию цен: ",', '.join(sorted(spisok_price,reverse=True)))
print()
print("Сортирорвка по возрастанию цен пяти самых дорогих: ", ', '.join(sorted(spisok_price)[-5:]))









