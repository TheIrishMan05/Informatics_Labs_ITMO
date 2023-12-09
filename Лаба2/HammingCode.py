s = input()
r1 = int(s[0])
r2 = int(s[1])
i1 = int(s[2])
r3 = int(s[3])
i2 = int(s[4])
i3 = int(s[5])
i4 = int(s[6])
s1 = r1 ^ i1 ^ i2 ^ i3
s2 = r2 ^ i1 ^ i3 ^ i4
s3 = r3 ^ i2 ^ i3 ^ i4
check_sum = str(s1) + str(s2) + str(s3)
match check_sum:
    case '011':
        i3 = int(not i3)
        print("Mistake has been detected and fixed in the byte i3.", end='\n')
        print(str(i1) + str(i2) + str(i3) + str(i4))
    case '101':
        i2 = int(not i2)
        print("Mistake has been detected and fixed in the byte i2.", end='\n')
        print(str(i1) + str(i2) + str(i3) + str(i4))
    case '110':
        i1 = int(not i1)
        print("Mistake has been detected and fixed in the byte i1.", end='\n')
        print(str(i1) + str(i2) + str(i3) + str(i4))
    case '111':
        i4 = int(not i4)
        print("Mistake has been detected and fixed in the byte i4.", end='\n')
        print(str(i1) + str(i2) + str(i3) + str(i4))
    case _:
        print("Mistakes haven't been detected or it occurred in the check_sum bytes.")
        print(str(i1) + str(i2) + str(i3) + str(i4))
