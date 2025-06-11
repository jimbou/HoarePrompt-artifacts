#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (2 <= n <= 2 * 10^5), then two binary strings of length n.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: Output State: a is a list containing two binary strings of length n, n is an integer between 2 and 2 * 10^5 inclusive, stdin contains multiple test cases - 1.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: Output State: s is a list containing a binary string of length n, x is an integer between 0 and n - 1 inclusive, a is a list containing two binary strings of length n, n is an integer between 2 and 2 * 10^5 inclusive.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: Output State: `t` is an integer between 1 and `n` inclusive.
    print(s, sep='')
    #This is printed: the value of s (where s is a string or a value that can be printed, but its exact value is unknown)
    print(t)
    #This is printed: the value of t (which is an integer between 1 and n inclusive)

#Overall this is what the function does:This function reads two binary strings of the same length from standard input, attempts to find a prefix of the first string that matches a suffix of the second string, and prints the resulting combined string and the length of the matching prefix. If no match is found, it prints the first string and the length of the entire string.

