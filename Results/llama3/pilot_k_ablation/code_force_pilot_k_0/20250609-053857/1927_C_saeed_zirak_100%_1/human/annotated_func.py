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
        
    #State: The output state after the loop executes all the iterations is a series of 'yes' or 'no' printed to the console, each corresponding to a test case. The 'yes' indicates that it is possible to make the two sets a and b have exactly k/2 ones in common by adding or removing elements, and 'no' indicates that it is not possible. The input state remains unchanged, with the same values for t, n, m, k, a, and b.

#Overall this is what the function does:The function reads input from the standard input, processes it, and prints a series of 'yes' or 'no' to the console, each corresponding to a test case. The function determines whether it is possible to make two sets have exactly k/2 ones in common by adding or removing elements, and prints 'yes' if possible and 'no' otherwise. The input state remains unchanged.

