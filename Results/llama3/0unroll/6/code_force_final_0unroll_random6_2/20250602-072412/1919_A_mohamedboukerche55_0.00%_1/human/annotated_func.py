#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) — the number of coins in Alice's and Bob's wallets, respectively.
    for i in range(int(input())):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
    #State: The loop has iterated over all test cases and extracted the values of a and b for each test case, but no further operations have been performed. The values of a and b are the last values read from the input for each test case.
    if ((a + b) % 2 == 0) :
        print('bob  ')
        #This is printed: bob
    else :
        print('alice')
        #This is printed: alice
    #State: *The loop has iterated over all test cases and extracted the values of a and b for each test case. The values of a and b are the last values read from the input for each test case. If the sum of a and b is even, 'bob' is being printed. If the sum of a and b is odd, 'alice' is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers representing the number of coins in Alice's and Bob's wallets. It then determines the parity of the sum of the coins in each test case and prints 'bob' if the sum is even or 'alice' if the sum is odd. The function processes all test cases and prints the corresponding result for each case.

