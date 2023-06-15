a = [True, False]

#первый вариант
flag = True
for x in a:
    for y in a:
        for z in a:
            if (not(x) and (not(y) or z) and (y or not(z))) != (not(x) and (not(y) or not(z)) and (y or not(z))):
                flag = False
if (flag == False):
    print("Первый вариант НЕ эквивалентен исходной формуле")
else:
    print("Первый вариант эквивалентен исходной формуле")

#второй вариант
flag = True
for x in a:
    for y in a:
        for z in a:
            if (not(x) and (not(y) or z) and (y or not(z))) != ((x or not(y) or not(z)) and (y or z)):
                flag = False
if (flag == False):
    print("Второй вариант НЕ эквивалентен исходной формуле")
else:
    print("Второй вариант эквивалентен исходной формуле")

#третий вариант
flag = True
for x in a:
    for y in a:
        for z in a:
            if (not(x) and (not(y) or z) and (y or not(z))) != (not(y) and (not(x) or z) and (not(x) or y or z)):
                flag = False
if (flag == False):
    print("Третий вариант НЕ эквивалентен исходной формуле")
else:
    print("Третий вариант эквивалентен исходной формуле")

#четвертый вариант
flag = True
for x in a:
    for y in a:
        for z in a:
            if (not(x) and (not(y) or z) and (y or not(z))) != ((not(x) or not(y)) and (not(x) or z)):
                flag = False
if (flag == False):
    print("Четвёртый вариант НЕ эквивалентен исходной формуле")
else:
    print("Четвёртый вариант эквивалентен исходной формуле")

#пятый вариант
flag = True
for x in a:
    for y in a:
        for z in a:
            if (not(x) and (not(y) or z) and (y or not(z))) != (not(x) and not(y) and (x or z)):
                flag = False
if (flag == False):
    print("Пятый вариант НЕ эквивалентен исходной формуле")
else:
    print("Пятый вариант эквивалентен исходной формуле")

