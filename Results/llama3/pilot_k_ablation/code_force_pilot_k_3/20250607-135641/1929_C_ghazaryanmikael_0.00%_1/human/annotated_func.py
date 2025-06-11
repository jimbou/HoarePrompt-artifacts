#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 0
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: `k` is an integer, `x` is an integer, `a` is an integer, `s` is `x` plus the sum of `x-1` times the integer division of the sum of the integer division of `s` by `k-1` and 1 by `k-1`, `_` is the number of test cases minus 1, `i` is `x-1`, `stdin` is empty, and either 'YES' or 'NO' is printed depending on whether `a` is greater than or equal to `s` or not.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case contains three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. The function continues processing test cases until the standard input is empty.

