#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a space-separated list of integers. The first integer is a positive integer (1 <= n <= 2 * 10^5). The list of integers contains n non-negative integers (0 <= a_i < n). The sum of n over all test cases does not exceed 2 * 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break
        
    #State: `stdin` is empty, `n` is not defined, `a` is not defined, `cntl` is not defined, `c` is not defined.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n non-negative integers. It then finds the smallest positive integer that is not present in the list or is present but has a count less than 2, and prints this integer. If no such integer is found, it prints 0. The function continues this process until all test cases have been read from standard input, leaving the input stream empty.

