#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line is an integer (1 <= n <= 5000) and the second line is a string of "+" and "-" of length n.
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
        
    #State: The output will be the absolute difference between the number of '+' and '-' characters in each string, for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer and a string of '+' and '-' characters. It then calculates and prints the absolute difference between the number of '+' and '-' characters in each string, for each test case.

