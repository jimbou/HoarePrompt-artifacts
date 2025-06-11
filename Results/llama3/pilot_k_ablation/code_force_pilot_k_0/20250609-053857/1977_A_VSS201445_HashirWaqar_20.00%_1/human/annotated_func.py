#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: The output state will contain 'YES' or 'NO' for each test case, indicating whether the given numbers n and m satisfy the conditions in the loop body. The number of lines in the output state will be equal to the number of test cases t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers n and m. It then checks each case against two conditions: (1) if n is less than m, it prints 'NO'; (2) if n and m are both odd or both even, it prints 'YES'. The function outputs 'YES' or 'NO' for each test case, indicating whether the given numbers satisfy the conditions. The number of output lines equals the number of test cases.

