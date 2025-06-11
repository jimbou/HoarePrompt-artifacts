#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. In each test case, at least one cell contains a chip.
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
        
    #State: t is 0, stdin is empty, and the number of zeros in arrs[sIdx:eIdx+1] has been printed for all test cases.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the count of zeros in a specific range of a binary array for each test case. It accepts no parameters and returns no values, but instead, prints the results directly. The function consumes all input from stdin and leaves it empty after execution.

