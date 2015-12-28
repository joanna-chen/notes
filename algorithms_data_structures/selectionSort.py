def selectionSort(li):
    count = len(li)-1
    greatest = None
    for n in range(len(li)-1):
        for i in range(len(li)-1):
            if li[i+1] > li[i]:
                greatest = li[i+1]
                spot = i+1
        li[spot],li[count] = li[count],li[spot]
        print(li)
        count = count - 1


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
