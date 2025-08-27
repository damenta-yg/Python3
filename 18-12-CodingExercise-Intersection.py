def intersection(list_a,list_b):
    to_return = []
    for i in list_a:
        for j in list_b:
            if i == j:
                to_return.append(i)
    return to_return


#intersection([1,2,3],[2,3,4])
