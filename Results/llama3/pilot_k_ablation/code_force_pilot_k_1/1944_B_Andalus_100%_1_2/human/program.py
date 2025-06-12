T = int (input ())
for _ in range (T):
    n, k = map (int, input().split())
    lst = list (map (int, input().split()))
    lft = lst[:n]
    rgt = lst[n:]
    ldb = []    # left half doubles
    rdb = []    # right half doubles
    sng = []    # singles
    
    lft.sort()
    rgt.sort()
    
    if lft[0] != lft[1]:
        sng.append (lft[0])
    for i in range (1, n):
        if lft[i] == lft[i - 1]:
            ldb.append (lft[i])
        elif i == n - 1 or lft[i] != lft[i + 1]:
            sng.append (lft[i])
    for i in range (1, n):
        if rgt[i] == rgt[i - 1]:
            rdb.append (rgt[i])
    
    #print (ldb, rdb, sng)
    
    
    sz = 0
    for elem in ldb:
        if 2 * k - sz >= 2:
            print (elem, elem, end=' ')
            sz += 2
        else:
            break
            
    for elem in sng:
        if sz >= 2 * k:
            break
        print (elem, end=' ')
        sz += 1
        
    print ()
    
    sz = 0
    for elem in rdb:
        if 2 * k - sz >= 2:
            print (elem, elem, end=' ')
            sz += 2
        else:
            break
        
    for elem in sng:
        if sz >= 2 * k:
            break
        print (elem, end=' ')
        sz += 1
        
    print ()