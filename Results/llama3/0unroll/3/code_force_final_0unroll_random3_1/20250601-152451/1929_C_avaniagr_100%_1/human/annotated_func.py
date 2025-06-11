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
        
    #State: The output state will contain a series of 'YES' or 'NO' for each test case, indicating whether the given value of 'a' is sufficient to meet the conditions based on the values of 'k' and 'x'.

#Overall this is what the function does:This function determines whether a given value 'a' is sufficient to meet certain conditions based on the values of 'k' and 'x' for multiple test cases, and outputs a series of 'YES' or 'NO' indicating the result for each test case.

