import re
with open('maintasktest.txt') as f:
    pat = re.compile(r'[rb]\[<\)', re.IGNORECASE)
    for i in f.readlines():
        print(pat.findall(i))

