#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers: k, x, and a. k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
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
        
    #State: `t` is an integer representing the number of test cases that must be 0, `k`, `x`, and `a` are integers that are the last three inputs from the stdin, `_` is `t`, stdin contains no test cases. If `x` is less than `k - 1`, then 'YES' is printed if `a` is greater than or equal to `x + 1`. If `x` is greater than or equal to `k - 1`, then 'YES' is printed if `x` is equal to `k - 1` and `a` is greater than or equal to `x + 3`, or if `x` is not equal to `k - 1` and `a` is greater than or equal to `z`. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers: k, x, and a. It then checks the conditions for each test case and prints 'YES' or 'NO' based on the following rules: if x is less than k-1, it prints 'YES' if a is greater than or equal to x+1; if x is equal to k-1, it prints 'YES' if a is greater than or equal to x+3; if x is greater than k-1, it calculates a value z and prints 'YES' if a is greater than or equal to z. Otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving the standard input empty.

