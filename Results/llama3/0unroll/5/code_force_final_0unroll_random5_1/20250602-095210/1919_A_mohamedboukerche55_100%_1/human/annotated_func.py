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
        
    #State: The output state will be a sequence of 'Bob' and 'Alice' printed to the console, where 'Bob' is printed if the sum of the two integers on a line is even, and 'Alice' is printed if the sum is odd. The number of lines in the output will be equal to the value of `t`. The value of `t` and the contents of stdin will remain unchanged.

#Overall this is what the function does:This function reads a sequence of integer pairs from standard input and prints a sequence of 'Bob' and 'Alice' to the console, where 'Bob' is printed for pairs with even sums and 'Alice' is printed for pairs with odd sums. The number of output lines equals the initial input integer `t`, and the input state remains unchanged.

