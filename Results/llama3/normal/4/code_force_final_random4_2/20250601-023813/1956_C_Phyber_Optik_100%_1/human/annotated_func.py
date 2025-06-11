#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: `t` is 0, `_` is `t`, `n` is an integer, `sum` is 1 + ∑((i * i - (i - 1) * (i - 1)) * i) for i from 2 to n, `stdin` is empty, `i` is `n + 1`, `j` is `n + 1`, and this is printed: 2, 1, and the numbers from 1 to `n`, and the value of `n`, and this is printed: the value of `sum` which is 1 + Σ((i * i - (i - 1) * (i - 1)) * i) from i = 2 to n, and the value of `n + n` which is 2 times the value of `n`

#Overall this is what the function does:The function reads a number of test cases from standard input, then for each test case, it reads an integer n and calculates a sum based on a formula involving squares of numbers up to n. It then prints the calculated sum and the value of n + n, followed by a series of lines containing the numbers from 1 to n, the value of n, and the numbers from 1 to n again. After processing all test cases, the function leaves the standard input empty.

