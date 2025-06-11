#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (2 <= n <= 2 * 10^5), then two binary strings of length n. The number of test cases (1 <= t <= 10^4) is given on the first line.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `a` is a list containing two binary strings of length `n`, `n` is an integer equal to the first input from stdin, stdin contains multiple test cases, each test case contains three inputs: first an integer (2 <= n <= 2 * 10^5), then two binary strings of length n, `_` is 2
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: a is a list containing two binary strings of length n, n is an integer at least 2, stdin contains multiple test cases, each test case contains three inputs: first an integer (2 <= n <= 2 * 10^5), then two binary strings of length n, _ is 2, s is a binary string of length n, x is an integer equal to n - 1.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: `a` is a list containing two binary strings of length `n`, `n` is an integer at least 2, `stdin` contains multiple test cases, each test case contains three inputs: first an integer (2 <= `n` <= 2 * 10^5), then two binary strings of length `n`, `_` is 2, `s` is a binary string of length `n`, `x` is an integer equal to `n - 1`, `i` is `n - 1`. If the first `i + 1` characters of the first binary string in `a` are equal to the first `i + 1` characters of `s`, then `t` is `x - i + 1`. Otherwise, `t` is 1.
    print(s, sep='')
    #This is printed: The binary string s of length n (where n is an integer at least 2)
    print(t)
    #This is printed: 1

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two binary strings of length n. It then attempts to find a prefix of the first binary string that matches a suffix of the second binary string, and if found, constructs a new binary string by concatenating the prefix with the suffix. The function prints the constructed binary string and the length of the prefix. If no matching prefix is found, it prints the first binary string and 1.

