#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle.
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: The loop has executed n times, and for each iteration, it has printed either 'YES' or 'NO' to the console based on the input values of a and b. The value of n remains unchanged. The stdin contains one less test case than initially.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers representing the size of a rectangle. It then determines whether it is possible to divide the rectangle into two equal parts by cutting it along a line that passes through the center of the rectangle, and prints 'YES' if possible, or 'NO' otherwise. The function processes all test cases and prints the results to the console, leaving the input unchanged.

