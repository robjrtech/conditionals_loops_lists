list = [64, 25, 12, 22, 11]

newlist = []

for num in list:
    if list[0] >= list[1]:
        newlist.append(num)
        print(sorted(newlist))