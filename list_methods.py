my_list = [1, 2, 3]
print(my_list)

my_list.append(4)   # [1, 2, 3, 4]
print(my_list)

my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
print(my_list)

my_list.remove(2)   # [1, 99, 3, 4]
print(my_list)

my_list.pop()       # Removes last element -> [1, 99, 3]
print(my_list)

my_list.reverse()   # [3, 99, 1]
print(my_list)

my_list.sort()      # [1, 3, 99]
print(my_list)