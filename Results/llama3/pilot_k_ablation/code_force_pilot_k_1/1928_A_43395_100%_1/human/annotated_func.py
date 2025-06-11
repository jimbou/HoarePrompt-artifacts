#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: stdin is empty, `i` is the number of test cases, `a` and `b` are the last two integers in the input, the output contains 'yes' or 'no' for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers a and b. It then determines whether a and b can be equal after a series of operations (halving a or b if they are even) and prints 'yes' if possible, 'no' otherwise. The function processes all test cases and empties the standard input, leaving the number of test cases and the last two integers in the input as residual values.

