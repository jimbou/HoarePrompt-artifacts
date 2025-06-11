#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
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
        
    #State: Output State: The variable 'l' will be 'YES' if for any test case, there exists a position where both strings 'a' and 'b' have different characters than string 'c', otherwise 'l' will be 'NO'. The variable 't' will remain unchanged as it is not modified within the loop.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs 'YES' if any test case has a position where both strings 'a' and 'b' differ from string 'c', otherwise outputs 'NO'. The function does not modify the input variable 't' and only uses it to control the number of test cases to process.

