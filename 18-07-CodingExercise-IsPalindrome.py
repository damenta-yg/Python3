def reverse_string(string):
    i = len(string)
    to_return = []
    while i > 0:
        to_return.append(string[i-1])
        i = i - 1
    return ''.join(to_return)

def is_palindrome(string):
    compare = reverse_string(string)
    if string == compare:
        return True
    return False



x = "hannah"
print(is_palindrome(x))