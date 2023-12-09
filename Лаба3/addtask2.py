import re


def add_task2(file):
    global test_letters
    a = file.readlines()
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    pat = re.compile(rf'\b\w*[{test_letters}]\w*[{test_letters}]\w*[{test_letters}]\w*\b')
    a = [line.rstrip() for line in a]
    print(a)
    n = 1
    i = 0
    ans = []
    flag = 1
    while i < len(a):
        print('Тест' + ' ' + str(n))
        if a[i].isdigit():
            rang = int(a[i]) + 1
            i += 1
            a_check = pat.findall(a[i])
            print(a_check)
            j = 0
            while j < len(a_check):
                s = a_check[j]
                for g in range(0, len(s), rang):
                    if s[g] not in alph:
                        flag = 0
                        break
                if flag == 1:
                    ans.append(s)
                    print(s)
                j += 1
        n += 1
        i += 1
    return ans


test_letters = input()
with open('additionaltask2test.txt', encoding='utf-8') as f:
    print(add_task2(f))
