def single_letter_count(str,character):
    to_check = str.lower()
    count = 0
    for i in to_check:
        if i == character:
            count = count + 1
    return count


print(single_letter_count("HELLO WORLD","x"))
