#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n (2 <= n <= 2 * 10^5), then two binary strings of length n. The sum of n over all test cases does not exceed 2 * 10^5.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: Output State: a is a list containing two binary strings of length n, n is an integer equal to the first input from stdin.
    s = []
    x = 0
    y = 0
    for i in range(n - 1):
        if a[0][i + 1] == '0' and a[1][i] == '1':
            y = i
        
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: Output State: The list s contains a binary string of length n, x is an integer between 0 and n - 1, y is an integer between 0 and n - 2, and a is a list containing two binary strings of length n.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: Output State: The list s contains a binary string of length n, x is an integer between 0 and n - 1, y is an integer between 0 and n - 2, a is a list containing two binary strings of length n, and t is the length of the longest suffix of s that matches a prefix of a[1].
    print(s, sep='')
    #This is printed: the binary string s (where s is a binary string of length n)
    print(t)
    #This is printed: t (where t is the length of the longest suffix of the binary string s that matches a prefix of the second binary string in the list a)

#Overall this is what the function does:This function reads two binary strings of the same length from standard input, modifies the first string by replacing a suffix with a corresponding suffix from the second string if a mismatch is found, and prints the modified string along with the length of the longest suffix of the modified string that matches a prefix of the second string.

