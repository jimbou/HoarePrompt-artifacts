#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The output will be a series of 'Alice' and 'Bob' printed to the console, with the number of lines equal to the value of 'test'. Each line will be either 'Alice' or 'Bob', depending on whether the sum of the two integers on the corresponding line of stdin is odd or even, respectively. The value of 'test' remains unchanged.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, determines whether the sum of each pair is odd or even, and prints 'Alice' for odd sums and 'Bob' for even sums, repeating this process a number of times specified by the first integer read from standard input.

