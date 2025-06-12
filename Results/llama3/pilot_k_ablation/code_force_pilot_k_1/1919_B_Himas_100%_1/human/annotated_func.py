#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines: the first line contains a positive integer n, and the second line contains a string s of length n consisting of characters "+" and "-".
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(abs(P - M))
        
    #State: stdin is empty, `i` is equal to the number of test cases, `s` is the last integer input, `e` is the last string input, `P` is the number of '+' characters in the last string input, `M` is the number of '-' characters in the last string input, and the absolute difference between the number of '+' characters and the number of '-' characters in each string input has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a string s of length n containing '+' and '-' characters. It then calculates and prints the absolute difference between the number of '+' and '-' characters in each string input. The function continues this process until all test cases have been read from standard input, leaving the input stream empty.

