#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length. The length of the binary strings is equal to the integer.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `a` is a list containing two strings, `n` is an integer, stdin contains multiple test cases minus four test cases. Each remaining test case contains three inputs: first an integer, then two binary strings of the same length. The length of the binary strings is equal to the integer, `_` is 2, range is at least 2
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: a is a list containing two strings, n is an integer, s is a string, x is an integer, _ is 2, range is at least 2, i is n - 2. Stdin contains multiple test cases minus four test cases. Each remaining test case contains three inputs: first an integer, then two binary strings of the same length. The length of the binary strings is equal to the integer. If a[0][i + 1] is '1' and a[1][i] is '0' for any i in range(n - 1), then s is a string that is a concatenation of the first i + 1 characters of a[0] and the rest of a[1], and x is equal to i. Otherwise, s is a string that is a concatenation of a[0] and the last character of a[1], and x is equal to n - 1.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: a is a list containing two strings, n is an integer, s is a string, x is an integer, _ is 2, range is at least 2, i is x - 1, t is x - i if a[0][:i + 1] == s[:i + 1], otherwise t is 1, stdin contains multiple test cases minus four test cases. Each remaining test case contains three inputs: first an integer, then two binary strings of the same length. The length of the binary strings is equal to the integer.
    print(s, sep='')
    #This is printed: the string s (where s is a binary string of a certain length)
    print(t)
    #This is printed: 1

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two binary strings of the same length. It then processes each test case to find the longest prefix of the first binary string that matches a suffix of the second binary string, and prints the resulting concatenated string and the length of the matching prefix. If no matching prefix is found, it prints the concatenation of the first binary string and the last character of the second binary string, along with a length of 1.

