# дз 5
"""
1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('zad_1.txt', 'w') as f:
    while True:
        data = input('введите данные для записи в файл: \n')
        if not data:
            break

        ''.join([data, '\n'])
        print(data, file=f)


"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
"""

with open('zad_2.txt') as f:
    text = f.readlines()
    print(f'количество строк в файле: {len(text)}')

    for i, elem in enumerate(text):
        print(f'в строке с номером {i + 1} слов: {len(elem.split())}')

    print('\n')

"""
3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
 (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
 Выполнить подсчет средней величины дохода сотрудников.
"""

with open('zad_3.txt', encoding='utf-8') as f:
    buff = f.readlines()

    money = 0
    for man in buff:
        surname, salary = man.split()
        if float(salary) < 20000:
            print(surname)

        money += float(salary)

    print(f'средняя величина дохода сотрудников: {money / len(buff) :.2f}\n')


"""
4) Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в 
новый текстовый файл.
"""

text = []
with open('zad_4.txt') as f:
    for line in f:
        text.append(line)

new_text = []
for line in text:
    if 'One' in line:
        new_text.append(''.join(['Один', line[3:]]))
    elif 'Two' in line:
        new_text.append(''.join(['Два', line[3:]]))
    elif 'Three' in line:
        new_text.append(''.join(['Три', line[5:]]))
    elif 'Four' in line:
        new_text.append(''.join(['Четыре', line[4:]]))

with open('new_zad_4.txt', 'w', encoding='utf-8') as nf:
    for line in new_text:
        nf.write(line)


"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('zad_5.txt', 'w') as f:
    buff = input('введите числа через пробел: ')
    f.write(buff)

with open('zad_5.txt') as f:
    numbers = f.readline()
    summ = 0
    for number in numbers.split():
        summ += float(number)

print(summ, '\n')


"""
6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
 были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
 Вывести словарь на экран.
"""

with open('zad_6.txt', encoding='utf-8') as f:
    buff = []
    for line in f:
        buff.append(line)

k_val_list = []
for el in buff:
    st_class = el.split()

    number = 0
    for val in st_class[1:]:
        number += int(val[:val.index('(')])

    k_val_list.append((st_class[0][:-1], number))

dictionary = {k: v for k, v in k_val_list}
print(dictionary)


"""
7) Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
 Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать
  словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить 
  ее в словарь (со значением убытков). Итоговый список сохранить в виде json-объекта в соответствующий файл

"""

import json

with open('zad_7.txt') as f:
    buff = []
    for line in f:
        buff.append(line)

av_prof = 0
k_v_list = []
for line in buff:
    inf = line.split()

    prof = float(inf[-2]) - float(inf[-1])
    k_v_list.append((inf[0], prof))
    print(f'прибыль компании {inf[0]} составляет {prof}')
    if prof < 0:
        continue

    av_prof += prof
else:
    av_prof /= len(buff)
    print(f'средняя прибыль всех компаний {av_prof}')

firms_dict = {k: v for k, v in k_v_list}
res_list = [firms_dict, {'average_profit': av_prof}]

with open('zad_7_json.json', 'w') as f_json:
    json.dump(res_list, f_json)
