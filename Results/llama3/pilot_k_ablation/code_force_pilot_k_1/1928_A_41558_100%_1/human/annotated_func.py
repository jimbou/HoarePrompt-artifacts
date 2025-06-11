#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases.
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: `n` is an integer between 1 and 10^4 (inclusive), `i` is equal to `n`, `a` and `b` are the last two integers read from stdin, stdin is empty.

#Overall this is what the function does:This function reads a specified number of test cases from standard input, where each test case consists of two integers representing the dimensions of a rectangle. It then determines whether it is possible to divide the rectangle into two equal halves with integer dimensions, printing 'YES' if possible and 'NO' otherwise. The function processes all test cases and leaves the input stream empty.

