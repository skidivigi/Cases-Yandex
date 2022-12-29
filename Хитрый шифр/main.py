a = input()
counter = 0
alphabet  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',\
                                                                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = int(a)
b = []
while counter != n:
    a = input()
    b.append(a.split(','))
    counter += 1

counter = 0
first_symbol = []
while counter != len(b):
    first = b[counter][0][0]
    first_symbol.append(alphabet.index(first.lower())+1)
    counter += 1

counter = 0
length = []

while counter != len(b):
    count = 0
    n = ''
    while count != 3:
        n += b[counter][count]
        count += 1
    count = len(set(n))
    length.append(count)
    counter += 1

counter = 0
characters = []
while counter != len(b):
    count = 0
    n = ''
    n = b[counter][3] + b[counter][4]
    for each in n:
        count += int(each)
    characters.append(count)
    counter += 1

counter = 0
total = []
while counter != len(b):
    count = hex(length[counter] + characters[counter] * 64 + first_symbol[counter] * 256)
    total.append(str(count))
    counter += 1

counter = 0
n = ''
while counter != len(b):
    n += total[counter][len(total[counter]) - 3:len(total[counter])] + ' '
    counter += 1

print(n.upper())


