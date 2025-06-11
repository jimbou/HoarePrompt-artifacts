#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: The output state will contain t lines, each containing an integer representing the minimum number of operations required to make a and b equal to m. The integer on each line will be the result of the if-elif-else statement inside the loop, which depends on the values of a, b, and m.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. It then calculates and prints the minimum number of operations required to make a and b equal to m, considering all possible cases where m is less than, greater than, or equal to a and b. The function outputs the results for each test case on a new line, with the number of operations being the sum of divisions of m by a and b, plus 2, depending on the relative values of a, b, and m.

