user_string = "*"

#print(user_string)

for i in range (1,10):
    temp_string = ""
    num = 0
    while num < i:
        temp_string += user_string
        num = num + 1
    print(temp_string)

