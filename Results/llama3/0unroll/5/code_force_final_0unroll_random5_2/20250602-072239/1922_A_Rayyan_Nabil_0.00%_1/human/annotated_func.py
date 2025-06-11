#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
    t = int(input())
    l = 'YES'
    for i in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        for i in range(n):
            if a[i] != c[i] and b[i] != c[i]:
                l = 'YES'
        else:
            l = 'NO'
        
        print(l)
        
    #State: Output State: The value of variable 'l' will be 'NO' if for all test cases, there exists at least one position where the characters in strings 'a' and 'c' are the same or the characters in strings 'b' and 'c' are the same. Otherwise, the value of 'l' will be 'YES'. The value of 't' will be 0. The value of 'stdin' will be empty.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether there exists at least one position in each test case where the characters in strings 'a' and 'c' are the same or the characters in strings 'b' and 'c' are the same. If such a position exists in all test cases, it outputs 'NO'; otherwise, it outputs 'YES'. The function consumes all input from stdin and leaves it empty after execution.

