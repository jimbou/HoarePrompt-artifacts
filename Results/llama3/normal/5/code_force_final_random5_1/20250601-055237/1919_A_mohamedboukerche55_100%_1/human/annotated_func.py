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
        
    #State: t is an integer between 1 and 1000 (inclusive), stdin is empty, i is t-1. If (a + b) is even for the last iteration, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, determines whether the sum of each pair is even or odd, and prints 'Bob' for even sums and 'Alice' for odd sums. The function processes a specified number of pairs, as indicated by an initial integer input, and then terminates, leaving the standard input empty.

