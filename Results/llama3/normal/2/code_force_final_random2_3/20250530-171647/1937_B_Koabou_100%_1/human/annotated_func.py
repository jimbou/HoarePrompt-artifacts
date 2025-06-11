#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two binary strings of the same length which is equal to the integer.
    a = []
    n = int(input())
    for _ in range(2):
        a.append(input())
        
    #State: `a` is a list containing two string inputs, `n` is an integer, stdin contains multiple test cases minus four test cases, `_` is 2, 2 is not greater than 2
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
        
    #State: a is a list containing two string inputs, n is an integer, _ is 2, s is a string that is a combination of the first i + 1 characters of the first string in a and the rest of the second string in a if a[0][i + 1] is '1' and a[1][i] is '0' for any i in range(n - 1), otherwise s is a string that is a combination of the first string in a and the last character of the second string in a, x is equal to the index of the character '1' in the second string of a if a[0][i + 1] is '1' and a[1][i] is '0' for any i in range(n - 1), otherwise x is n - 1, y is equal to the index of the character '1' in the second string of a if a[0][i + 1] is '0' and a[1][i] is '1' for any i in range(n - 1), otherwise y is not changed, i is n - 2, stdin contains multiple test cases minus four test cases.
    t = 1
    for i in range(y, x):
        if a[1][i:x] == s[i + 1:x + 1]:
            t = x - i + 1
            break
        
    #State: `a` is a list containing two string inputs, `n` is an integer, `_` is 2, `s` is a string that is a combination of the first i + 1 characters of the first string in `a` and the rest of the second string in `a` if `a[0][i + 1]` is '1' and `a[1][i]` is '0' for any `i` in range(`n` - 1), otherwise `s` is a string that is a combination of the first string in `a` and the last character of the second string in `a`, `x` is equal to the index of the character '1' in the second string of `a` if `a[0][i + 1]` is '1' and `a[1][i]` is '0' for any `i` in range(`n` - 1), otherwise `x` is `n` - 1, `y` is equal to the index of the character '1' in the second string of `a` if `a[0][i + 1]` is '0' and `a[1][i]` is '1' for any `i` in range(`n` - 1), otherwise `y` is not changed and is less than `x`, `i` is `x`, `t` is `x` - `i` + 1 if `a[1][i:x]` is equal to `s[i + 1:x + 1]`, otherwise `t` is 1, stdin contains multiple test cases minus four test cases if `a[1][i:x]` is not equal to `s[i + 1:x + 1]`, otherwise stdin contains multiple test cases minus five test cases.
    print(s, sep='')
    #This is printed: A string that is a combination of the first i + 1 characters of the first string in `a` and the rest of the second string in `a` if `a[0][i + 1]` is '1' and `a[1][i]` is '0' for any `i` in range(`n` - 1), otherwise a string that is a combination of the first string in `a` and the last character of the second string in `a`
    print(t)
    #This is printed: x - i + 1 (if a[1][i:x] is equal to s[i + 1:x + 1]) or 1 (if a[1][i:x] is not equal to s[i + 1:x + 1])

#Overall this is what the function does:This function reads two binary strings of the same length from standard input, combines them into a new string by replacing a prefix of the first string with a suffix of the second string, and prints the combined string along with the length of the longest suffix of the second string that matches a prefix of the combined string. If no such suffix is found, it prints 1. The function processes multiple test cases from standard input.

