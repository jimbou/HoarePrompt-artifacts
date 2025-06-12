#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: `n` is an integer, `a` is a list of integers, `cntl` is a list of `n+1` integers where the value at index `i` is the number of occurrences of `i` in `a`, `stdin` is empty, `_` is the number of test cases, `c` is either 0 or 1 or 2, and `j` is between 1 and `n` (inclusive) if the loop executed at least once, otherwise `j` is 1. If the loop executed, either `c` is 0 or `cntl[j]` is 0. If the loop did not execute, `n` is 0.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds the smallest positive integer missing from the list, or 0 if the list is empty or contains only zeros. The function prints the result for each test case.

