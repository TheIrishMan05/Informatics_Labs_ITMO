import timeit


def task_5(file):
    strings = file.read().split('\n')
    for i in range(len(strings)):
        strings[i] = strings[i].replace('    ', '')
    return strings


time5 = []
for k in range(100):
    with open('C:\study\labs\инфа\Лаба4\Вторник.yml', 'r', encoding="utf-8") as input_f:
        full_file = task_5(input_f)
    with open('C:\study\labs\инфа\Лаба4\Вторник.txt', 'w', encoding="utf-8") as output_f:
        for j in range(len(full_file)):
            output_f.write(full_file[j] + '\n')
    time5.append(timeit.timeit())
print(str((min(time5) + max(time5)) / 2) + ' - addtask 5')
