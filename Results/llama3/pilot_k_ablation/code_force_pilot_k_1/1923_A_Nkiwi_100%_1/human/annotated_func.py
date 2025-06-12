#State of the program right berfore the function call: stdin contains t+2t lines, where t is an integer (1 <= t <= 1000). The first line contains t. Each of the following t pairs of lines contains an integer n (2 <= n <= 50) and a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 1), such that at least one a_i is 1.
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
        
    #State: `t` is 0, `stdin` is empty, `length` is not defined, `arrs` is not defined, `sIdx` is not defined, `eIdx` is not defined, `cnt0` is not defined, `i` is not defined.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no value. It reads a series of test cases, where each test case consists of a length and a list of integers. It then finds the first and last non-zero elements in the list, counts the number of zeros between them, and prints this count. After processing all test cases, the function leaves the program in a state where all input has been consumed and all variables used within the function are no longer defined.

