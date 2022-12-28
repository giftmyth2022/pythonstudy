#搜索

def LinearSearch(list,item):
    index = 0
    found = False
    while index <len(list) and found is False:
        if list[index] == item:
            found =True
        else:
            index = index +1
    return found

list = [1,33,95,65,46,52,32,61,20,30,36,99,25]
print(LinearSearch(list,99))