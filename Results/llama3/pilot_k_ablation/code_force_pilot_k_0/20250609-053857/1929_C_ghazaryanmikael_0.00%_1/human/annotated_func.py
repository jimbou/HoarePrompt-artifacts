#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 0
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: The output state will be a series of 'YES' or 'NO' for each test case, indicating whether the value of 'a' is greater than or equal to the calculated sum 's'. The number of 'YES' or 'NO' will be equal to the number of test cases provided in the input.

#Overall this is what the function does:Determines whether a given value 'a' is greater than or equal to a calculated sum 's' for multiple test cases, and outputs 'YES' or 'NO' accordingly.

