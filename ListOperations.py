# Q4 List Operation

#Python Code- 
my_list = [1, 2, 3, 4, 5]

print(my_list[0])
print(my_list[2])

my_list.append(6)
print(my_list)

my_list.remove(3)
print(my_list)

for i in my_list:
    print(i)

print(my_list[1:4])

print(len(my_list))



# Output
# 1
# 3
# [1, 2, 3, 4, 5, 6]
# [1, 2, 4, 5, 6]
# 1
# 2
# 4
# 5
# 6
# [2, 4, 5]
# 5
