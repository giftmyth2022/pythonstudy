def SelectSort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in  range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
    return list



arr= [8,5,4,3,6,9,1,2]

print(SelectSort(arr))
