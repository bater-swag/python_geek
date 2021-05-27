import codecs

'''
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

file = open('first.txt', 'w')
info = input('Введите текст')
while info:
    file.write(info + '\n')
    info = input('Введите текст или пустую строку для выхода')
    if not info:
        break
file.close()
'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
'''
col_line = 0
with open('second.txt', "r") as file:
    for line in file:
        print(f'Строка номер:{col_line}, количество слов в строке: {len(line.split())}')
        col_line += 1
print(f'Всего строк: {col_line}')

'''
3. Создать текстовый файл (не программно), построчно записать фамилии 
сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад 
менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней 
величины дохода сотрудников.
'''


with codecs.open('third.txt', "r", "utf_8_sig") as file:
    second_names = []
    zarplata = []
    for line in file:
        info = line.split()
        zarplata.append(info[1])
        if int(info[1]) < int('20000'):
            second_names.append(info[0])

print(
    f'Оклад меньше 20.000 {second_names}, средний оклад {sum(map(int, zarplata))/len(zarplata)}')

'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
dict_number = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре',
               'Five': 'Пять'}
new_info = []
with open('four.txt', "r") as file:
    for line in file:
        info = line.split(' -')
        new_info.append(dict_number[info[0]]+' -'+info[1])

with open('four_new.txt', 'w') as file_2:
    file_2.writelines(new_info)

'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и 
выводить ее на экран.
'''
with open('five.txt', 'w') as file:
    numbers = input('Введите числа через пробел')
    file.writelines(numbers)

with open('five.txt', 'r') as file:
    for line in file:
        sum = sum(map(int, line.split()))
        print(f'Сумма чисел: {sum}')

'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает 
учебный предмет и наличие лекционных, практических и лабораторных занятий по 
этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и 
общее количество занятий по нему. Вывести словарь на экран.
'''
import re


def take_number(line):
    res = re.findall(r'\d+', line)
    if len(res) >= 1:
        return res[0]
    else:
        return '0'


info = {}
with codecs.open('six.txt', "r", "utf_8_sig") as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        info[subject] = int(take_number(lecture)) + int(
            take_number(practice)) + int(take_number(lab))
print(f'Общее количество часов по предметам - \n {info}')

'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна 
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также 
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить 
ее в словарь (со значением убытков).
'''
import json

profit = {}
prof = 0
col = 0
res = []
with codecs.open('seven.txt', "r", "utf_8_sig") as file:
    for line in file:
        name, type_f, pribl, izder = line.split()
        profit[name] = int(pribl) - int(izder)
        res.append(profit)
        if profit[name] >= 0:
            prof += profit[name]
            col += 1
    if col != 0:
        aver_prof = prof/col
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    avg_pr = {'средняя прибыль': round(aver_prof)}
    res.append(avg_pr)

with open('seven.json', 'w') as file_1:
    json.dump(res, file_1)