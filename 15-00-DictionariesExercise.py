#138
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}
for index,key in enumerate(list1):
    answer[key] = list2[index]
    
print(answer)


#140
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0] : person[i][1] for i in range(len(person))}


print(answer)


#141
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {num : chr(num) for num in range(65,91)}

print(answer)