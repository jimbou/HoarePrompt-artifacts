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
        
    #State: `n` is 0, `i` is `n`, `a` and `b` are integers assigned from the input, stdin contains multiple test cases minus `n` test cases. If both `a` and `b` are odd numbers, then 'NO' is printed. If either `a` is even or `b` is even or both are even, then if `a` is equal to 2 times `b` and `b` is odd or `b` is equal to 2 times `a` and `a` is odd, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers representing the size of a rectangle. It then checks each test case and prints 'YES' if the rectangle can be divided into 2x1 tiles without any leftovers, and 'NO' otherwise. The function continues this process until all test cases have been processed.

