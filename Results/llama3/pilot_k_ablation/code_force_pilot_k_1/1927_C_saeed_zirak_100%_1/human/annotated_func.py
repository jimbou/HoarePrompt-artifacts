#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three integers n, m, and k (1 <= n, m <= 2*10^5, 2 <= k <= 2*min(n, m), k is even) followed by two lists of integers a and b of lengths n and m respectively (1 <= a_i, b_j <= 10^6).
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = frozenset(map(int, input().split()))
        
        b = frozenset(map(int, input().split()))
        
        leftOnes = 0
        
        aOnes = 0
        
        bOnes = 0
        
        newk = k // 2
        
        i = 1
        
        while i <= k:
            if i in a and i in b:
                leftOnes += 1
            elif i in a:
                aOnes += 1
            elif i in b:
                bOnes += 1
            else:
                break
            i += 1
        
        i = 0
        
        while i < leftOnes:
            if aOnes < bOnes:
                aOnes += 1
            else:
                bOnes += 1
            i += 1
        
        if aOnes == newk and bOnes == newk:
            print('yes')
        else:
            print('no')
        
    #State: stdin is empty, `t` is 0, `n`, `m`, `k`, `a`, `b`, `newk`, `i`, `leftOnes`, `aOnes`, `bOnes` are undefined.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether it's possible to make two sets of numbers equal by adding a certain number of ones to each set. It prints 'yes' if it's possible and 'no' otherwise. The function does not modify the input sets or any other external state, and it does not return any value. After execution, stdin is empty, and all variables used within the function are undefined.

