#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 5000) and then a string s of length n consisting of characters "+" and "-".
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
        
    #State: `i` is equal to the initial number of test cases, `s` is an integer, `e` is a string, `P` is the number of '+' characters in the last string `e`, `M` is the number of characters in the last string `e` that are not '+', `stdin` is empty, and the absolute difference between the number of '+' characters and the number of characters that are not '+' in each string `e` has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing '+' and '-' characters. It then calculates and prints the absolute difference between the number of '+' characters and the number of '-' characters in each string. The function processes all test cases and empties the standard input.

