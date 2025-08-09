list_1 = [1,2,3,4]
list_2 = [3,4,5,6]

new_list_1 = [num for num in list_1 if num in list_2]
print(new_list_1)


list_2 = ["Ellie"]
new_list_2 = [new_str[::-1].lower() for new_str in list_2]

print(new_list_2)