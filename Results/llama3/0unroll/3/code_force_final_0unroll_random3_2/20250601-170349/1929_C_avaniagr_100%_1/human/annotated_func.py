#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers: k, x, and a. k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case, indicating whether the value of 'a' is greater than or equal to the calculated value 'z' or not.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers: k, x, and a. It then determines whether the value of 'a' is greater than or equal to a calculated value 'z' based on the values of 'k' and 'x'. The function prints 'YES' to the console if 'a' is greater than or equal to 'z', and 'NO' otherwise, for each test case.

