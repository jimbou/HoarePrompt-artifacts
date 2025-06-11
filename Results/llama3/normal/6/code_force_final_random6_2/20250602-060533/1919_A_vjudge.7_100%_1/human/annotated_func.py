#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `test` is 0, `t` is equal to the initial value of `test`, stdin is empty. The number of 'Bob's and 'Alice's printed is equal to the initial value of `test`.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers. It then determines the winner of each case based on the sum of the two integers being even or odd, printing 'Bob' for even sums and 'Alice' for odd sums. The function continues this process until all test cases have been read from standard input, ultimately emptying the input buffer.

