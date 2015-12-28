def bubbleSort(li):
    for n in range(len(li)-1):
        for i in range(len(li)-1):
            if li[i] > li[i+1]:
                temp = li[i+1]
                li[i+1] = li[i]
                li[i] = temp
    print(li)

bubbleSort([54,26,93,17,77,31,44,55,20])

def shortBubbleSort(li):
    exchanges = True
    while exchanges == True:
        for i in range(len(li)-1):
            if li[i] > li[i+1]:
                temp = li[i+1]
                li[i+1] = li[i]
                li[i] = temp
            else:
                exchanges = False
                break
    print(li)

shortBubbleSort([20,30,40,90,50,60,70,80,100,110])
