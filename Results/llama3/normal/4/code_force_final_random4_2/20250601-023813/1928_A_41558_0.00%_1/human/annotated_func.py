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
        
    #State: `n` is at least `n`, `i` is `n-1`, `a` and `b` are integers from the input. If both `a` and `b` are odd, 'NO' is printed. If `a` is twice `b` or `b` is twice `a`, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function determines whether a given rectangle can be partitioned into 2x1 dominoes. It accepts multiple test cases as input, where each test case consists of two integers representing the dimensions of the rectangle. The function then checks each test case and prints 'YES' if the rectangle can be partitioned into 2x1 dominoes and 'NO' otherwise. The function handles cases where both dimensions are odd or where one dimension is twice the other, in which case it prints 'NO'. For all other cases, it prints 'YES'.

