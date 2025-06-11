#State of the program right berfore the function call: stdin contains a sequence of lines. The first line contains a single integer t (1 <= t <= 10^4). Each of the next t lines contains a single integer n (2 <= n <= 500). Each of the next t lines contains n-1 space-separated integers x_2,...,x_n (1 <= x_i <= 500).
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: `n` is an integer at least 2, `i` is `n-1`, `x` is a list of `n-1` integers between 1 and 500, `a` is a list of `n` integers where the first element is 1000, the second element is 1000 + `x[0]`, the third element is 1000 + `x[0]` + `x[1]`, and so on, until the `n`th element which is 1000 + `x[0]` + `x[1]` + ... + `x[n-2]`, stdin contains 0 lines, and the list `a` is printed.

#Overall this is what the function does:The function reads a sequence of lines from standard input, where the first line contains the number of test cases, and each test case consists of two lines: the first line contains an integer n, and the second line contains n-1 space-separated integers. The function then generates a list of n integers, where the first element is 1000, and each subsequent element is the sum of the previous element and the corresponding integer from the input list. The function prints each generated list. The function repeats this process for the specified number of test cases, until all input lines have been processed.

