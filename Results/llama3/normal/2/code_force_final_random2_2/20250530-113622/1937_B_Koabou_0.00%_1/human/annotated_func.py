#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (n), then two binary strings of length n.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `a` is a list containing two strings, `n` is an integer, stdin contains multiple test cases minus three test cases, `_` is 2, the integer `2` is at least 1
    s = []
    x = 0
    for i in range(n - 1):
        if a[0][i + 1] == '1' and a[1][i] == '0':
            s = a[0][:i + 1] + a[1][i:]
            x = i
            break
        
    #State: a is a list containing two strings, n is an integer, stdin contains multiple test cases minus three test cases, _ is 2, the integer 2 is at least 1, s is a string containing a[0][0], a[0][1], ..., a[0][i], and a[1][i], where i is the smallest integer such that a[0][i + 1] is '1' and a[1][i] is '0', and x is i, or if no such i exists, then s is a string containing a[0] and a[1][n - 1], and x is n - 1, and i is n - 1.
    t = 1
    for i in range(x):
        if a[0][:i + 1] == s[:i + 1]:
            t = x - i + 1
            break
        
    #State: a is a list containing two strings, n is an integer, stdin contains multiple test cases minus three test cases, _ is 2, the integer 2 is at least 1, s is a string containing a[0][0], a[0][1], ..., a[0][i], and a[1][i], where i is the smallest integer such that a[0][i + 1] is '1' and a[1][i] is '0', and x is i, or if no such i exists, then s is a string containing a[0] and a[1][n - 1], and x is n - 1, and i is n - 1, and t is 1 if a[0][:i + 1] equals s[:i + 1], otherwise t is x - i + 1, i is x - 1, x must be greater than or equal to 0.
    print(s, sep='')
    #This is printed: a string containing a[0][0], a[0][1], ..., a[0][i], and a[1][i], where i is the smallest integer such that a[0][i + 1] is '1' and a[1][i] is '0', or if no such i exists, then a string containing a[0] and a[1][n - 1]
    print(t)
    #This is printed: 1 if a[0][:i + 1] equals s[:i + 1], otherwise x - i + 1 (where x is i, or n - 1, and i is the smallest integer such that a[0][i + 1] is '1' and a[1][i] is '0', or n - 1 if no such i exists)

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and two binary strings of length n. It then finds the smallest index i such that the first string's (i+1)th character is '1' and the second string's ith character is '0'. If such an index exists, it constructs a new string s by concatenating the first i+1 characters of the first string and the ith character onwards of the second string. If no such index exists, it constructs s by concatenating the entire first string and the last character of the second string. The function then finds the length of the longest prefix of s that is equal to the corresponding prefix of the first string. Finally, it prints the constructed string s and the length of the longest matching prefix.

