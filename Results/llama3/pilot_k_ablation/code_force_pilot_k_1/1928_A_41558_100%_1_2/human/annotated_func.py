#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle.
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: `n` is an integer (0 <= n <= 10^9), `i` is `n`, `a` and `b` are integers. If `n` is 0, no output is printed. If `n` is greater than 0, the loop prints 'YES' or 'NO' for each test case.

#Overall this is what the function does:The function reads an integer n from standard input, representing the number of test cases. For each test case, it reads two integers a and b, representing the size of a rectangle. It then checks if the rectangle can be divided into two equal smaller rectangles by checking if either a or b is even, or if one is twice the other and the other is odd. If the rectangle can be divided, it prints 'YES', otherwise it prints 'NO'. If n is 0, no output is printed.

