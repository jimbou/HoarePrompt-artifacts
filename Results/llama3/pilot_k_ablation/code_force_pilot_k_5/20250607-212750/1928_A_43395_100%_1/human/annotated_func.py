#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle.
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: `i` is equal to the number of test cases, stdin is empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers representing the size of a rectangle. It then determines whether the rectangle can be divided into two equal smaller rectangles and prints 'yes' if possible, 'no' otherwise. The function processes all test cases and leaves the standard input empty after execution.

