#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 5000). The second line contains a string s of length n consisting of characters "+" and "-".
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
        
    #State: stdin is empty, s is 0, e is an empty string, P is 0, M is 0, i is the number of test cases, and the absolute difference between the number of '+' characters and the number of '-' characters in each string e has been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string s of length n containing '+' and '-' characters. It calculates the absolute difference between the number of '+' and '-' characters in each string and prints this difference for each test case. After processing all test cases, the function leaves the standard input empty and does not return any value.

