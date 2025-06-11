#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: Output State: The loop will execute t times, each time printing the result of the expression m // a + m // b + 2. The output will be t lines, each containing the result of the expression for the corresponding input values of a, b, and m.

#Overall this is what the function does:The function reads a series of input lines from standard input, where the first line contains an integer t, representing the number of test cases, and each subsequent line contains three integers a, b, and m. For each test case, the function calculates and prints the result of the expression m // a + m // b + 2. The function executes this process t times, producing t lines of output, each containing the calculated result for the corresponding input values of a, b, and m.

