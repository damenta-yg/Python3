def last_element(elements):
    if type(elements).__name__ != "list" or len(elements) <= 0:
        return None
    else:
        return elements[-1]



print(last_element(1))