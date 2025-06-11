#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (2 <= n <= 2 * 10^5), then two binary strings a and b of length n.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: Output State: a is a list containing two binary strings of length n, n is an integer between 2 and 2 * 10^5 (inclusive), stdin contains multiple test cases with two binary strings a and b of length n minus two test cases.
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: Output State: s is a list containing two binary strings of length n, x is an integer between 0 and n - 1 (inclusive).
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: Output State: `s` is a list containing two binary strings of length n, `x` is an integer between 0 and n - 1 (inclusive), `t` is the maximum value of `x - i + 1` for `i` in range `x` such that `a[0][:i + 1] == s[:i + 1]`, or 1 if no such `i` exists.
    print(s, sep='')
    #This is printed: the concatenation of the two binary strings in the list s
    print(t)
    #This is printed: t (where t is the maximum value of x - i + 1 for i in range x such that the first i + 1 characters of the first binary string in the list s are equal to the first i + 1 characters of the second binary string in the list s, or 1 if no such i exists)

#Overall this is what the function does:This function reads two binary strings of the same length from standard input, modifies the second string by replacing its prefix with the corresponding prefix from the first string if the first string has a '1' at a position where the second string has a '0', and then prints the modified string and the length of the longest common prefix between the modified string and the first string.

