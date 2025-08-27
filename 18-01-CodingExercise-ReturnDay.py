def return_day(num):
    list_day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num <= 0 or num > 7:
        return None
    else:
        return list_day[num-1]


print(return_day(8))