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
        
    #State: Output State: The list s contains the binary string formed by concatenating the first i + 1 characters of the first binary string in a and the last n - i - 1 characters of the second binary string in a, where i is the index at which the first mismatch between the two binary strings was found, x is equal to i, and y is equal to the index of the last mismatch between the two binary strings. If no mismatch was found, s contains the concatenation of the first binary string in a and the last character of the second binary string in a, and x is equal to n - 1.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: Output State: The list s contains the binary string formed by concatenating the first i + 1 characters of the first binary string in a and the last n - i - 1 characters of the second binary string in a, where i is the index at which the first mismatch between the two binary strings was found, x is equal to i, and y is equal to the index of the last mismatch between the two binary strings. If no mismatch was found, s contains the concatenation of the first binary string in a and the last character of the second binary string in a, and x is equal to n - 1. Additionally, t is assigned the value x - i + 1.
    print(s, sep='')
    #This is printed: The binary string s (where s is the binary string formed by concatenating the first i + 1 characters of the first binary string in a and the last n - i - 1 characters of the second binary string in a, or the concatenation of the first binary string in a and the last character of the second binary string in a if no mismatch was found)
    print(t)
    #This is printed: 1

#Overall this is what the function does:This function reads two binary strings of the same length from standard input and outputs a new binary string formed by concatenating the prefix of the first string and the suffix of the second string, where the prefix and suffix are determined by the first mismatch between the two input strings. If no mismatch is found, the function outputs the concatenation of the first string and the last character of the second string. Additionally, the function prints the length of the longest common suffix between the second input string and the output string.

