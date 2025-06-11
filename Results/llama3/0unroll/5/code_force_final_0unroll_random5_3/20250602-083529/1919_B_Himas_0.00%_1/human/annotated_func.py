#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
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
        
        print(P - M)
        
    #State: The output will be the difference between the number of '+' and '-' characters in each string, for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing '+' and '-' characters. It then calculates and prints the difference between the number of '+' and '-' characters in each string, for each test case.

