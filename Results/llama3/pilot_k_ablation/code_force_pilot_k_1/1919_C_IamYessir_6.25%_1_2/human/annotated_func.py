#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [lit[0]], []
        
        cp = 0
        
        for i in range(1, n):
            if a[-1] < lit[i]:
                b.append(lit[i])
            else:
                a.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: `stdin` is empty, `n` is not defined, `lit` is not defined, `a` is not defined, `b` is not defined, `cp` is not defined, `s` is not defined, `_` is the number of test cases, `i` is not defined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes each test case by splitting the list into two lists, a and b, based on the condition that a list contains increasing numbers and b list contains non-increasing numbers. Finally, it counts the number of adjacent pairs in both lists where the second number is greater than the first and prints this count for each test case, leaving the standard input empty after processing all test cases.

