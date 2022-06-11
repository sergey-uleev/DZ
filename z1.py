# сумма ряда
print(sum(range(0, 88888888)))

# среднее арифметическое ряда
number = [3, 4, 56, 100, 2, 2, 3]
summa = 0
kol = len(number)
while number != []:
    s = number.pop()
    summa += s / kol
print(summa)

# заменить в строчке все х на y
a = 'asdxfghyxyx'
print(a.replace('x', 'y'))

# Сосчитать сумму чисел кратных 3 и 5
a = [3, 4, 56, 100, 15, 2, 20, 30]
sp = 1
for i in a:
    if i % 3 == 0 and i % 5 == 0:
        sp *= i
print(sp)
