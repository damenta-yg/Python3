def compact(list):
    to_return = []
    for i in list:
        if bool(i) is True:
            to_return.append(i)
    #print(to_return)
    return to_return


#print(2 == True)
print(compact([0,1,2,"",[], False, {}, None, "All done"]))