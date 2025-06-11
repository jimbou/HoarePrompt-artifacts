#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers: k, x, and a, where k is an integer between 2 and 30, x is an integer between 1 and 100, and a is an integer between 1 and 10^9.
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
        
    #State: `t` is a positive integer greater than or equal to 0, `k`, `x`, and `a` are integers that are the first, second, and third integers from the last test case in stdin, stdin contains no test cases. If `x` is less than `k-1`, then if `a` is greater than or equal to `x + 1`, 'YES' is printed. Otherwise, 'NO' is printed. If `x` equals `k-1`, then if `a` is greater than or equal to `x + 3`, 'YES' is printed. Otherwise, 'NO' is printed. If `x` is greater than or equal to `k-1` but not equal to `k-1`, then `z` is `x+1` plus `x` times the integer division of 1 by `k-1`, `x` is greater than or equal to 0, `i` is `x`. If `a` is greater than or equal to `z`, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers: k, x, and a. It then checks the conditions for each test case and prints 'YES' if the condition is met, and 'NO' otherwise. The conditions are as follows: if x is less than k-1, it checks if a is greater than or equal to x+1; if x is equal to k-1, it checks if a is greater than or equal to x+3; if x is greater than or equal to k-1, it calculates a value z based on x and k, and checks if a is greater than or equal to z. The function processes all test cases and prints the corresponding results.

