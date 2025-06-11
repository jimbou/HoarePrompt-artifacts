#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is 0, `itest` is `t`, `n`, `m`, and `k` are integers between 1 and 50, stdin is empty. The loop has finished executing, and all the output has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers n, m, and k. It then determines whether it is possible to satisfy a certain condition based on these integers and prints 'Yes' if possible, 'NO' otherwise. The function processes all test cases and prints the corresponding results, ultimately consuming all input and producing output for each test case.

