t = int(input())
 
for _ in range(t):
    length = int(input())
    arrs = list(map(int, input().split()))
 
    sIdx = 0
    eIdx = length - 1
 
 
    while sIdx < length and arrs[sIdx] == 0:
        sIdx += 1
    
    while eIdx >= 0 and arrs[eIdx] == 0:
        eIdx -= 1
 
    cnt0 = 0
 
    for i in range(sIdx, eIdx + 1):
        if arrs[i] == 0:
            cnt0 += 1
 
    print(cnt0)