#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: i is t-1, a is an integer between 1 and 10^9 inclusive, b is an integer between 1 and 10^9 inclusive, stdin is empty
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: *i is t-1, a is an integer between 1 and 10^9 inclusive, b is an integer between 1 and 10^9 inclusive, stdin is empty. If the sum of a and b is even, 'bob ' is printed. If the sum of a and b is odd, 'alice' is printed.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, determines whether the sum of each pair is even or odd, and prints 'bob' if the sum is even or 'alice' if the sum is odd.

