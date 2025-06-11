#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle.
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The output state will be a series of 'Yes' or 'No' printed to the console, one for each test case, indicating whether the sum of the dimensions of Bob's rectangle is even or odd. The value of `t` will be unchanged, and the contents of stdin will be consumed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers representing the dimensions of a rectangle. It then determines whether the sum of these dimensions is even or odd and prints 'Yes' if the sum is even and 'No' if the sum is odd, one output per test case. The function consumes the contents of standard input and leaves the value of the test case counter unchanged.

