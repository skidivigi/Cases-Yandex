with open('input.txt', 'r') as file:
    src = file.read().split('\n')
src = src[1:len(src)]

elem = 0
for each in src:
    if len(each) == 1:
        elem = each
    else:
        continue

drc = src[src.index(elem)+1:len(src)]
src = src[0:src.index(elem)]


recipes, counter, count = {}, 3, 0

while counter != len(src) + 3:
    intermediate = []
    for i in src[count]:
        if i != ' ':
            intermediate.append(i)
        continue
    intermediate = intermediate[1:len(intermediate)]
    recipes[str(counter)] = intermediate
    count += 1
    counter += 1

total, counter, count = '', 0, 0

while counter != len(drc):
    intermediate, list = [], []
    t_a, t_b = 0, 0
    for i in drc[counter]:
        if i != ' ':
            intermediate.append(i)
        continue
    number = recipes[intermediate[-1]]
    intermediate = intermediate[0:len(intermediate)-1]
    while count != len(src):
        for i in number:
            if i not in '12':
                number.remove(i)
                number += recipes[i]
            continue
        count += 1
    for i in number:
        if i == '1':
            t_a += 1
        else:
            t_b += 1
    if int(intermediate[0]) >= t_a and int(intermediate[1]) >= t_b:
        total += '1'
    else:
        total += '0'
    counter += 1

print(total)