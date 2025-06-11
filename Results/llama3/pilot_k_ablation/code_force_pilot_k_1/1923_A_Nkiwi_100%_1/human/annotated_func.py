#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 1).
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
        
    #State: `t` is 0, `stdin` is empty, `sIdx` is not defined, `eIdx` is not defined, `cnt0` is not defined, `length` is not defined, `arrs` is not defined.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n binary digits (0s and 1s). It then counts the number of zeros in the middle of each test case, excluding leading and trailing zeros, and prints the count. The function processes all test cases and leaves the input stream empty.

