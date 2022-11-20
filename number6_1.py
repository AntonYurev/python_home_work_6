# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) 
# и дополнить нулём до двух целочисленных разрядов:
spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(spisok)):
    if "+" in spisok[i] or "-" in spisok[i]:
        if len(spisok[i]) == 2:
            spisok[i]=spisok[i][:1]+"0"+spisok[i][1:]
        spisok[i]='"'+spisok[i]+'"'
    elif spisok[i].isdigit():
        if len(spisok[i]) == 1:
            spisok[i]="0"+spisok[i]
        spisok[i]='"'+spisok[i]+'"'
print(" ".join(spisok))

