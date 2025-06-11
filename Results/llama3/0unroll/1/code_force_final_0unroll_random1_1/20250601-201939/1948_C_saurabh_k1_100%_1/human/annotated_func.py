#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines: the first line contains a single integer (n) such that 2 <= n <= 2 * 10^5 and n is even; the second and third lines contain strings consisting of exactly n characters '<' and/or '>'.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: The loop will print 'yes' or 'no' for each test case, indicating whether the given strings can be rearranged to form a valid sequence of '<' and '>' characters. The value of `t` remains unchanged, and the input strings `a` and `b` are not modified. The output will be a series of 'yes' or 'no' statements, one for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: an even integer n, and two strings of length n containing '<' and/or '>' characters. It then checks if the characters in the two strings can be rearranged to form a valid sequence of '<' and '>' characters. For each test case, it prints 'yes' if the strings can be rearranged, and 'no' otherwise. The function does not modify the input strings or the value of t, and only prints the result for each test case.

