#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 5000) — the length of string s. The second line contains string s (s_i ∈ {+, -}, |s| = n).
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
        
    #State: The output will be the difference between the number of '+' and '-' characters in each string, printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a string of '+' and '-' characters. It calculates and prints the difference between the number of '+' and '-' characters in each string, one output per test case.

