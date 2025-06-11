#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 5000) and the second line contains a string s of length n consisting of characters "+" and "-".
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
        
    #State: i is equal to the number of test cases, s is an integer, e is an empty string, stdin is empty, P is equal to the number of '+' characters in the last string e, M is equal to the number of '-' characters in the last string e, and the absolute difference between the number of '+' characters and '-' characters in the last string e is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing '+' and '-' characters. It then calculates the absolute difference between the number of '+' and '-' characters in each string and prints the result. The function processes all test cases and empties the standard input.

