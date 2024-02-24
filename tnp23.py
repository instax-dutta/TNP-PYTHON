y_values = [2,3,5,3,1,0,8]

max_area = 0
for i in range(len(y_values) - 1):
    width = 1
    height = min(y_values[i], y_values[i + 1])
    area = width * height
    max_area = max(max_area, area)

print(max_area)