#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a, where k is an integer between 2 and 30 (inclusive), x is an integer between 1 and 100 (inclusive), and a is an integer between 1 and 10^9 (inclusive).
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: `t` is an integer between 0 and 29 (inclusive), `_` is equal to `t`, `k`, `x`, `a` are integers assigned values from the input, stdin is empty. If `x` is less than `k - 1`, then 'YES' is printed if `a` is greater than or equal to `x` plus 1, otherwise 'NO' is printed. If `x` equals `k - 1`, then 'YES' is printed if `a` is greater than or equal to `x + 3`, otherwise 'NO' is printed. If `x` is greater than `k - 1`, then `z` is calculated as `x+1` plus the sum of the integer divisions of `i` by `k-1` for `i` from 0 to `x`, and 'YES' is printed if `a` is greater than or equal to `z`, otherwise 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers: k, x, and a. It then checks the value of x in relation to k and prints 'YES' if a is greater than or equal to a calculated value based on x and k, otherwise it prints 'NO'. The calculated value is x+1 if x is less than k-1, x+3 if x equals k-1, or a more complex calculation involving the sum of integer divisions if x is greater than k-1. The function processes all test cases and empties the standard input.

