#second max in a given list 
numbers = [20, 30, 40, 25, 10]
max1 = max2 = float('-inf')
for num in numbers:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num
print(max2)
