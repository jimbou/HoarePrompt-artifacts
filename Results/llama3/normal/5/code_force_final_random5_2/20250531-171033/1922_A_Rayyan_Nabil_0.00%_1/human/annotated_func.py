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
        
    #State: t is an integer between 1 and 1000, l is 'YES' if there exists at least one i where a[i] is not equal to c[i] and b[i] is not equal to c[i], otherwise 'NO', stdin is empty, and 'YES' or 'NO' is printed depending on whether there exists at least one i where a[i] is not equal to c[i] and b[i] is not equal to c[i].

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case. It checks if there exists at least one position where the characters in strings a and b are different from the character in string c. If such a position is found, it prints 'YES', otherwise it prints 'NO'. The function consumes all input from stdin and does not return any value.

