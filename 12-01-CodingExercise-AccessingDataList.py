# DON'T TOUCH THIS PLEASE!
people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

# Change "Hanna" to "Hannah"
for index,person in enumerate(people):
    if people[index] == "Hanna":
        people[index] = "Hannah"
        break

print(people)

# Change "Geoffrey" to "Jeffrey"
for index,person in enumerate(people):
    if people[index] == "Geoffrey":
        people[index] = "Jeffrey"
        break
print(people)

# Change "aparna" to "Aparna" (capitalize it)
for index,person in enumerate(people):
    if people[index] == "aparna":
        people[index] = "Aparna"
        break
print(people)