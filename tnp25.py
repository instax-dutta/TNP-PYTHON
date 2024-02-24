#print the pattern according to the list values approach 2
list = [1, 3, 2, 4, 6, 1]
max_value = max(list)

for i in range(max_value, 0, -1):
    line = ""
    for value in list:
        line += "*" if value >= i else " "
    print(line)


