#!usr/bin/pyshon3
def uniq_add(my_list=[]):
    new = []
    sum = 0
    for num in my_list:
        if num not in new:
            sum += num
            new.append(num)
    return num
