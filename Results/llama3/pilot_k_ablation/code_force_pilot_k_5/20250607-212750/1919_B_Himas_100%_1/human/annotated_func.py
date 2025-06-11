#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 5000). The second line contains a string s of length n consisting of characters "+" and "-".
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
        
    #State: stdin contains no test cases, i is equal to the number of test cases, s is an integer equal to the last input value, e is a string equal to the last input value, P is the number of '+' characters in the string e, M is the number of '-' characters in the string e, and the absolute difference between P and M is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing '+' and '-' characters. It then calculates the absolute difference between the number of '+' and '-' characters in the string and prints the result. The function processes all test cases and prints the absolute difference for each case.

