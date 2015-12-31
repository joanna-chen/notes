def quickSort(li):
    rquickSort(li,0,len(li)-1)

def rquickSort(li,first,last):
    if first < last:
        splitpoint = partition(li,first,last)

    rquickSort(li,first,splitpoint-1)
    rquickSort(li,splitpoint+1,last)

def partition(li,first,last):
    pivotvalue = li[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and li[leftmark] <= pivotvalue:
            leftmark += 1

        while li[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True

        # swap the leftmark and the rightmark when they are not on the right side
        else:
            temp = li[leftmark]
            li[leftmark] = li[rightmark]
            li[rightmark] = temp

    # swap the pivot value into where it belongs, the splitpoint
    temp = li[first]
    li[first] = li[rightmark]
    li[rightmark] = temp

    return rightmark
