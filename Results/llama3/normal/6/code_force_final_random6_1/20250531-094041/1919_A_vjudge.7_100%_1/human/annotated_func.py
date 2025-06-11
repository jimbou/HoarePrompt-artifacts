#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `test` is an integer between 1 and 1000 (inclusive), `t` is `test-1`, `a` and `b` are integers between 1 and 10^9 (inclusive) and are the values of the last line of the stdin, stdin contains 0 lines, and either 'Bob' or 'Alice' is being printed depending on whether the sum of `a` and `b` is even or odd.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers. It then determines whether the sum of these two integers is even or odd and prints 'Bob' if the sum is even, or 'Alice' if the sum is odd. The function processes all test cases and prints the corresponding result for each case.

