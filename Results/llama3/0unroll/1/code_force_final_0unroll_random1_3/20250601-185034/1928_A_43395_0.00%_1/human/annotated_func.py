#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9) — the size of Bob's rectangle. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases.
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: The output state will contain multiple lines, each containing either 'yes' or 'no'. The number of lines will be equal to the number of test cases. For each test case, if both a and b are even, the output will be 'yes'. If the difference between a and b is odd, the output will be 'yes'. Otherwise, the output will be 'no'.

#Overall this is what the function does:Determines whether the difference between two integers is even or odd for multiple test cases and outputs 'yes' if the difference is even or if both numbers are even, otherwise outputs 'no'.

