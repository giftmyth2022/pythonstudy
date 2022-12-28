def BubbleSort(list):
    for i in range(len(list)-1):
        for i in range(len(list)-1-i):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list

def BinarySearch(list,item):
    first = 0
    last = len(list)-1
    found = False

    while first <= last and found is False:
        midpoint = (first+last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item<list[midpoint]:
                last = midpoint -1
            else:
                last = midpoint +1
    return found

list = [1,33,95,65,46,52,32,61,20,30,36,99,25]
sortedList = BubbleSort(list)
print(BinarySearch(list,20))
print(BinarySearch(list,21))