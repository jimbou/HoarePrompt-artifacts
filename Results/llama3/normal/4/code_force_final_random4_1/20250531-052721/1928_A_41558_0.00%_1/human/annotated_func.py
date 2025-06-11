#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9) representing the size of Bob's rectangle.
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: `n` is an integer between 1 and 10^4 (inclusive), `i` is `n`, `a` and `b` are integers between 1 and 10^9 (inclusive) representing the size of Bob's rectangle, stdin contains multiple lines of input, where the first `n` lines have been read and the remaining lines contain two integers a and b (1 <= a, b <= 10^9) representing the size of Bob's rectangle. If both `a` and `b` are odd numbers, 'NO' is printed. If either `a` is even or `b` is even or both are even, then if `a` is twice `b` or `b` is twice `a`, 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:Determines whether a rectangle can be cut into two identical smaller rectangles based on its dimensions. The function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains two integers representing the dimensions of the rectangle. It then prints 'YES' if the rectangle can be cut into two identical smaller rectangles and 'NO' otherwise, considering the cases where both dimensions are odd or one dimension is twice the other.

