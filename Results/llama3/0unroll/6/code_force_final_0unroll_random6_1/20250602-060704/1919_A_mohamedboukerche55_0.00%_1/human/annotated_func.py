#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000) representing the number of test cases. Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9) representing the number of coins in Alice's and Bob's wallets, respectively.
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: The loop has iterated t times, and the variables a and b have been updated t times with the values from the input lines. The values of a and b are the last values read from the input lines. The rest of the execution state remains unchanged.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: The loop has iterated t times, and the variables a and b have been updated t times with the values from the input lines. The values of a and b are the last values read from the input lines. The rest of the execution state remains unchanged. If the sum of the current values of a and b is even, 'bob' is printed. If the sum of a and b is odd, 'alice' is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains two integers representing the number of coins in Alice's and Bob's wallets. After reading all input lines, the function prints 'bob' if the sum of the last two integers read is even, and 'alice' if the sum is odd. The function does not modify the input values or perform any other actions beyond printing the result.

