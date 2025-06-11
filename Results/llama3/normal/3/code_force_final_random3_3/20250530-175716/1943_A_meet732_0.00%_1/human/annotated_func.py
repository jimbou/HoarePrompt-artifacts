#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: `n` is an integer, `a` is an empty list, `cntl` is a list of integers with a length of `n + 1` where the value at each index `i` is equal to the number of times `i` appears in the original list `a`, `_` is equal to the number of test cases, `i` is the last integer in the original list `a`, `j` is `n`, and stdin is empty. If `cntl[0]` is 0, then 0 is printed. Otherwise, `c` is 0 and the value at index 0 of `cntl` is not equal to 0.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then counts the occurrences of each integer in the list and prints the smallest integer that appears at least twice, or 0 if no such integer exists. If the list contains no zeros, it prints 0. The function processes all test cases and prints the results accordingly.

