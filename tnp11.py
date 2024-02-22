def rotate_list(list1, r):
    n = len(list1)
    r = r % n  
    list1[:] = list1[-r:] + list1[:-r]
    return list1

# Example usage
list1 = [1, 2, 3, 4, 5]
r = 2

rotated_list = rotate_list(list1, r)
print(rotated_list)

# Output: [4, 5, 1, 2, 3]