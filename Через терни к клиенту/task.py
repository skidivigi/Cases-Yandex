with open('input.txt', 'r') as file:
    src = file.read().split('\n')
n = src[0]
src = src[1:len(src)]
total = []

for each in src:
    src = each.split(' ')
    total.append(src)

number = set()
for each in total:
    number.add(int(each[3]))
number = list(number)

length = ''
minuts = 0
counter = 0
while counter != len(number):
    alltracks = []
    for each in total:
        if int(each[3]) == number[counter]:
            alltracks.append(each)
        continue
    print(alltracks)
    h = 0
    m = 0
    minuts = 0
    for each in alltracks:
        if each[4] == 'A':
            for i in alltracks:
                if i[4] == 'B' and int(i[0]) in range(int(each[0]),int(each[0])+2):
                    print(i)
                    for cs in alltracks:
                        if cs[4] in 'CS' and int(cs[0]) in range(int(i[0]), int(i[0])+2):
                            if int(cs[0]) > int(i[0]):
                                if int(cs[2]) < int(i[2]):
                                    h = -(int(cs[1]) - int(i[1]))
                                    h = 24 - h
                                    m = (h * 60) - (int(i[2]) - int(cs[2]))
                                    minuts += m
                                    m = 0
                                    h = 0
                                else:
                                    h = -(int(cs[1]) - int(i[1]))
                                    h = 24 - h
                                    m = (h * 60) + (int(cs[2]) - int(i[2]))
                                    minuts += m
                                    m = 0
                                    h = 0
                            else:
                                if int(cs[2]) > int(i[2]) and int(cs[1]) >= int(i[1]):
                                    minuts += int(cs[2]) - int(i[2])
                                    minuts += (int(cs[1]) - int(i[1])) * 60
                                elif int(cs[2]) < int(i[2] and int(cs[1]) > int(i[1])):
                                    m += int(i[2]) - int(cs[2])
                                    minuts += ((int(cs[1]) - int(i[1])) * 60) - m
                                    m = 0
                                continue
                        continue
                    if i[4] == 'B' and int(i[0]) in range(int(each[0]), int(each[0]) + 2):
                        if int(i[2]) > int(each[2]) and int(i[1]) >= int(each[1]):
                            minuts += int(i[2]) - int(each[2])
                            minuts += (int(i[1]) - int(each[1])) * 60
                        elif int(i[2]) < int(each[2]) and int(i[1]) > int(each[1]):
                            m += int(each[2]) - int(i[2])
                            minuts += ((int(i[1]) - int(each[1])) * 60) - m
                            m = 0
                        continue
                    continue
            for io in alltracks:
                if io[4] == 'C' and int(io[0]) in range(int(each[0]), int(each[0])+2):
                    if int(io[2]) > int(each[2]) and int(io[1]) >= int(each[1]):
                        minuts += int(io[2]) - int(each[2])
                        minuts += (int(io[1]) - int(each[1])) * 60
                    elif int(io[2]) < int(each[2]) and int(io[1]) > int(each[1]):
                        m += int(each[2]) - int(io[2])
                        minuts += ((int(io[1]) - int(each[1])) * 60) - m
                        m = 0
                    continue
                continue
        continue


    length += str(minuts) + ' '
    counter += 1
print(length)

