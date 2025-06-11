#State of the program right berfore the function call: s is a string consisting of only 0-s and/or 1-s.
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is a string consisting of only 0-s and/or 1-s, `i` is `len(s)`, `n` is the number of '1's in `s`, `ans` is the sum of `n + 1` for each '0' in `s` that is not the first character and is preceded by at least one '1'.
    print(ans)
    #This is printed: the sum of (n+1) for each '0' in s that is not the first character and is preceded by at least one '1' (where n is the number of '1's in s)

#Overall this is what the function does:This function takes a string of binary digits as input, counts the number of consecutive '1's preceding each '0', and returns the sum of these counts plus one for each '0' that is not the first character and is preceded by at least one '1'.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer between 0 and 10^4 (inclusive), stdin contains `t` lines, each containing a binary string `s` (2 <= |s| <= 2 * 10^5), _ is `t-1`, a function named func_1 has been called and returned, func_1 has been called `t-1` more times.

#Overall this is what the function does:Reads an integer t from standard input, followed by t lines of binary strings, and calls a function named func_1 for each line, without modifying the input or returning any value.

