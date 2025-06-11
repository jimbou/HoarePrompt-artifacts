#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: `stdin` is empty, `n` is not defined, `a` is not defined, `cntl` is not defined.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then finds the smallest positive integer that is not present in the input integers for each test case, printing this integer. If the smallest missing positive integer is 1, it prints 0 instead. The function continues this process until all test cases have been processed, leaving the standard input empty.

