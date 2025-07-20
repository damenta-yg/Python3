# Initially create an empty list called instructors

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

# Run the tests to make sure you've done this correctly!
instructors = []
instructors.append("Colt")
instructors.extend(["Blue"])
instructors.insert(len(instructors),"Lisa")
print(instructors)