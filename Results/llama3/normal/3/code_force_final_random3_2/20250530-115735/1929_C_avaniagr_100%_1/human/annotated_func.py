#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: `k`, `x`, and `a` are integers and have been assigned the values from the last line of the last test case, stdin contains multiple test cases with at least as many lines as the number of iterations of the loop, `s` is no longer assigned as it has been used to assign values to `k`, `x`, and `a` in each iteration. If `x` is less than `k - 1`, then if `a` is greater than or equal to `x + 1`, 'YES' is printed. Otherwise, 'NO' is printed. If `x` is greater than or equal to `k - 1`, then if `x` equals `k - 1`, 'YES' is printed if `a` is greater than or equal to `x + 2`, otherwise 'NO' is printed. If `x` is not equal to `k - 1`, then `z` is an integer equal to `(x - k + 3) * (2 * k - 3 + (k - 2) // (k - 1)) // (k - 1) + 2 * k - 3 + (k - 2) // (k - 1) + (x - k + 2)`, `x - k + 3` is greater than or equal to 0, `i` is `x - k + 2`. If `a` is greater than or equal to `z`, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers k, x, and a. It then checks the conditions for each test case and prints 'YES' or 'NO' based on whether the value of a is greater than or equal to a calculated value z, which depends on the values of k and x. The function iterates through all test cases and prints the result for each case.

