#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: i is t-1, a is an integer between 1 and 10^9 inclusive, b is an integer between 1 and 10^9 inclusive, stdin contains 0 lines of input
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: *i is t-1, a is an integer between 1 and 10^9 inclusive, b is an integer between 1 and 10^9 inclusive, stdin contains 0 lines of input. If the sum of a and b is even, 'bob' is printed. Otherwise, 'alice' is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each subsequent line contains two integers a and b. It then checks if the sum of a and b is even or odd and prints 'bob' if the sum is even and 'alice' if the sum is odd. The function repeats this process t times, consuming all input lines from stdin.

