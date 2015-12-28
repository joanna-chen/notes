def mergeSort(li):
    if len(li) > 1:
        half = len(li)//2
        leftHalf = li[:half]
        rightHalf = li[half:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                li[k] = leftHalf[i]
                i += 1
            else:
                li[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            li[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            li[k] = rightHalf[j]
            j += 1
            k += 1

    print(li)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
