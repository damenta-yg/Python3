def multiple_letter_count(str):
    to_return = {}
    for i in str:
        if(to_return.get(i) == None):
            to_return[i] = 1
        else:
            to_return[i] = to_return[i] + 1
    return to_return


print(multiple_letter_count("hello"))