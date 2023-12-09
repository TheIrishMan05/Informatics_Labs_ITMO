import re
import timeit


def regexp_parse(f):
    global double_lessons
    case_1 = re.compile(r'\b.+:$')
    case_2 = re.compile(r'- .+:$')
    case_3 = re.compile(r'.+: ".+"$')
    strings = f.read()
    strings = re.sub("\n", "", strings)
    strings = re.sub("---", "", strings)
    arr_strings = strings.split('  ')
    arr_strings = [i for i in arr_strings if i != ""]
    final = "{\n"
    ar_count = 0  # промежуточный подсчёт элементов пар(кроме последнего)
    total_count = 0  # общий подсчёт элементов пар
    for i in range(len(arr_strings)):
        if case_1.match(arr_strings[i]):
            arr_strings[i] = '  ' + '"' + arr_strings[i].replace(':', '') + '": [\n' + '    {\n'
            final += arr_strings[i]
        elif case_2.match(arr_strings[i]):
            arr_strings[i] = arr_strings[i].replace('- ', '')
            arr_strings[i] = '      ' + '"' + arr_strings[i].replace(':', '') + '": {\n'
            final += arr_strings[i]
        elif case_3.match(arr_strings[i]):
            if ar_count < 3:
                arr_strings[i] = '        ' + '"' + arr_strings[i][:arr_strings[i].find(':')] + '": ' + \
                                 arr_strings[i][arr_strings[i].find(':') + 2:] + ',\n'
                final += arr_strings[i]
                ar_count += 1
            elif ar_count == 3:
                total_count += ar_count
                if total_count != double_lessons * ar_count:
                    arr_strings[i] = '        ' + '"' + arr_strings[i][:arr_strings[i].find(':')] + '": ' + \
                                     arr_strings[i][
                                     arr_strings[i].find(':') + 2:] + '\n      }\n' + '    },\n' + '    {\n'
                    final += arr_strings[i]
                    ar_count = 0
                else:
                    arr_strings[i] = '        ' + '"' + arr_strings[i][:arr_strings[i].find(':')] + '": ' + \
                                     arr_strings[i][arr_strings[i].find(':') + 2:] + '\n      }\n' + '    }\n  ]\n}'
                    final += arr_strings[i]
                    ar_count = 0
    return final


double_lessons = int(input())
time3 = []
for j in range(100):
    with open('C:\study\labs\инфа\Лаба4\Вторник.yml', 'r', encoding="utf-8") as file:
        a = regexp_parse(file)
    with open('C:\study\labs\инфа\Лаба4\Вторник(итог)(для тестов).json', 'w', encoding="utf-8") as output_file:
        output_file.write(a)
        time3.append(timeit.timeit())
print(str((min(time3) + max(time3)) / 2)  + ' - addtask2')