with open('input.txt', 'r') as file:
    src = file.read().split('\n')

src = src[1:len(src)]
elem = 0
for each in src:
    if len(each) == 1:
        elem = each

drc = list(map(str.split, src[src.index(elem)+1: len(src)]))
src = list(map(str.split, src[0: src.index(elem)]))
total = ''

for i in drc:
    intermediate = 0
    if i[2] == '1':
        for each in src:
            if int(each[0]) in range(int(i[0]), int(i[1])+1) or int(each[1]) in range(int(i[0])+1, int(i[1])):
                intermediate += int(each[2])
            else:
                continue
    else:
        for each in src:
            if int(each[0]) in range(int(i[0]), int(i[1])) or int(each[1]) in range(int(i[0]), int(i[1])+1):
                intermediate += int(each[1]) - int(each[0])
            else:
                continue
    total += str(intermediate) + ' '

print(total)