#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9) representing the size of Bob's rectangle.
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The loop will have printed 'Yes' or 'No' to the console t times, where 'Yes' is printed if either a or b is even, and 'No' is printed if both a and b are odd. The value of t remains unchanged.

#Overall this is what the function does:This function reads a number of test cases from standard input, then for each test case, it reads two integers representing the dimensions of a rectangle and prints 'Yes' if at least one dimension is even, or 'No' if both dimensions are odd. The function does not return any value, only prints the results to the console.

