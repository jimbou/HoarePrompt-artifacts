#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of exactly n lowercase Latin letters.
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
        
    #State: t is an integer between 1 and 1000, l is 'YES' if there exists at least one i such that a[i] != c[i] and b[i] != c[i] in any of the test cases, otherwise l is 'NO', i is t, n is an integer, a is a string of n lowercase Latin letters, b is a string of n lowercase Latin letters, c is a string of n lowercase Latin letters, stdin is empty.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' if at least one test case has a mismatch between strings a and c, and strings b and c, at the same position, otherwise prints 'NO'. The function consumes all input from stdin and leaves it empty.

