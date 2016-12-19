# keep track of index to move along, have sublist
def insertion(li):
    sublist = [li[0]]
    for i in range(1,len(li)):
        put = 0
        for subi in range(len(sublist)):
            if li[i] > sublist[subi]: 
                put = subi + 1
        sublist.insert(put, li[i])
    return sublist

print insertion([3,5,4])
