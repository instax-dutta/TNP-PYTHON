#print pattern in tnp23.py code horizontally according to the list values approach 1
list = [1, 3, 2, 4, 6, 1]
max_value = max(list)

for i in range(max_value, 0, -1):
    line = ""
    for value in list:
        if value >= i:
            line += "* "
        else:
            line += "  "
    print(line.rstrip())
