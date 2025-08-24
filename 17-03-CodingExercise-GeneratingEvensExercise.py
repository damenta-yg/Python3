def generate_evens():
    to_return = []
    for i in range(1,50):
        if i%2 == 0:
            to_return.append(i)
    return to_return

print(generate_evens())