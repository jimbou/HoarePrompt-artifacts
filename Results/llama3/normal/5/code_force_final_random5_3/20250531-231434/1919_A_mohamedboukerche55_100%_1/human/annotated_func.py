#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: t is an integer between 1 and 1000 (inclusive), i is t-1, a is an integer between 1 and 10^9 (inclusive), b is an integer between 1 and 10^9 (inclusive), stdin is empty, s is a string containing a space-separated list of two integers, a and b are integers between 1 and 10^9 (inclusive). If the sum of a and b is even, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input and determines whether the sum of each pair is even or odd. For each pair, it prints 'Bob' if the sum is even and 'Alice' if the sum is odd. The function processes a specified number of pairs, as indicated by an initial integer input.

