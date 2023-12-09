import re
with open('additionaltask1test.txt', encoding='utf-8') as f:
    a = f.readlines()
    pat = re.compile(r'\b\w*[аеёиоуыэюя]{2}\w*(?!\s+\b(?:[аеёиоуыэюя]*[бвгджзйклмнпрстфхцчшщ][аеёиоуыэюя]*){4,}|\s*$)\b', flags=re.IGNORECASE)
    a = [line.rstrip() for line in a]
    i = 0
    n = 1
    for i in range(len(a)):
        print(pat.findall(a[i]))

