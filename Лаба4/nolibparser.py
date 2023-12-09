def no_lib_parse(file):
    strings = file.readlines()
    strings = [line.rstrip() for line in strings]
    strings = [i for i in strings if i != ""]
    final = "{\n"
    space = ' '
    tab = '    '
    ar_count = 0
    for i in range(1, len(strings)):
        if strings[i].count(space) == 0:
            strings[i] = 2 * space + '"' + strings[i][:strings[i].find(':')] + '": [\n'
            final += strings[i]
        elif strings[i].count(tab) == 1:
            strings[i] = tab + '{\n' + 6 * space + '"' + \
                    strings[i][strings[i].find("-") + 2: strings[i].find(':')] + '": {\n'
            final += strings[i]
        elif strings[i].count(tab) == 2:
            if ar_count < 3:
                strings[i] = tab * 2 + '"' + strings[i][strings[i].rfind(space, 0, 8) + 1: strings[i].find(':')] + \
                                 '":' + \
                    strings[i][strings[i].find(':') + 1:] + ",\n"
                final += strings[i]
                ar_count += 1
            elif ar_count == 3:
                strings[i] = tab * 2 + '"' + strings[i][strings[i].rfind(space, 0, 8) + 1: strings[i].find(':')] + \
                        '":' + \
                    strings[i][strings[i].find(':') + 1:] + "\n" + 6 * space + '}\n' + tab + '},\n'
                final += strings[i]
                ar_count = 0
    final = final[:final.rfind(6 * space + '}\n' + tab + '},\n')] + \
            final[final.rfind(6 * space + '}\n' + tab + '},\n')].replace(6 * space + '}\n' + tab + '},\n', '')
    final += "     }\n    }\n  ]\n}"
    return final


with open('Вторник.yml', 'r', encoding="utf-8") as inputf:
    a = no_lib_parse(inputf)
with open('Вторник(итог)(для тестов).json', 'w', encoding="utf-8") as outputf:
    outputf.write(a)
