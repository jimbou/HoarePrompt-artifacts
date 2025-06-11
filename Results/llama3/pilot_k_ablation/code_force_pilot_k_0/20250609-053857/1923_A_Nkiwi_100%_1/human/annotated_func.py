#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. In each test case, at least one cell contains a chip.
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
        
    #State: The loop will print the number of zeros between the first and last occurrence of 1 in each test case, and the value of t will remain unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads an integer n and an array of n integers, where 0 represents a free cell and 1 represents a cell containing a chip. The function then finds the first and last occurrence of a chip (1) in the array, counts the number of free cells (0) between these two occurrences, and prints this count. The function repeats this process for all t test cases, leaving the value of t unchanged.

