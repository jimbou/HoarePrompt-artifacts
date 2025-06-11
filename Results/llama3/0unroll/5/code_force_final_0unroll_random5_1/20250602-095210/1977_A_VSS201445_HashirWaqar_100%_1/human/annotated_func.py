#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The output will contain 'YES' or 'NO' for each test case, indicating whether the condition (n >= m and (n - m) % 2 == 0) is met or not.

#Overall this is what the function does:Determines whether the difference between two input integers is even and the first integer is greater than or equal to the second, printing 'YES' if the condition is met and 'NO' otherwise, for multiple test cases.

