#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9) representing the size of Bob's rectangle.
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer between 1 and 10^4, `a` and `b` are integers between 1 and 10^9, `_` is `t-1`, stdin contains no lines of input. If either `a` or `b` is even, 'Yes' is printed. If both `a` and `b` are odd, 'No' is printed, and then 'Yes' is printed `t-1` times.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains two integers (a and b) representing the size of a rectangle. It then checks each rectangle's dimensions and prints 'Yes' if either dimension is even, and 'No' if both dimensions are odd. The function repeats this process for all test cases, printing 'Yes' for the remaining cases if the first case has both odd dimensions.

