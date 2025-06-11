#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (n), then two binary strings of length n.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `a` is a list containing two test cases, `n` is an integer, stdin contains multiple test cases minus three test cases, `_` is 2, and the integer `2` is not greater than 2.
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
        
    #State: a is a list containing two test cases, n is an integer, stdin contains multiple test cases minus three test cases, _ is 2, the integer 2 is not greater than 2, s is a list containing the first x elements of a[0] and the last len(a[1]) - x elements of a[1], x is an integer equal to the value of i that caused the loop to break, and y is equal to the value of i that caused the loop to break.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: a is a list containing two test cases, n is an integer, stdin contains multiple test cases minus three test cases, _ is 2, the integer 2 is not greater than 2, s is a list containing the first x elements of a[0] and the last len(a[1]) - x elements of a[1], x is an integer equal to the value of i that caused the loop to break, y is less than x, i is x - 1, and t is x - (x - 1) + 1.
    print(s, sep='')
    #This is printed: The first x elements of the first test case a[0] followed by the last len(a[1]) - x elements of the second test case a[1], where x is the value of i that caused the loop to break
    print(t)
    #This is printed: 2

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (n) and two binary strings of length n. It then attempts to find a prefix of the first binary string and a suffix of the second binary string that can be combined to form a new binary string. If such a combination is found, it prints the resulting binary string and the length of the overlapping suffix. If no combination is found, it does not print anything. The function processes each test case independently and does not retain any information from previous test cases.

