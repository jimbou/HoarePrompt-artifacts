#State of the program right berfore the function call: s is a binary string (a string consisting of only 0-s and/or 1-s) and the length of s is at least 2.
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is a binary string, `i` is equal to the length of `s`, `n` is equal to the number of '1's in `s`, and `ans` is the sum of all `n + 1` for each '0' in `s` where `n` is not 0.
    print(ans)
    #This is printed: sum of all n + 1 for each '0' in the binary string s where n is not 0 (where n is the number of '1's in s)

#Overall this is what the function does:The function takes a binary string as input and returns the sum of all `n + 1` for each '0' in the string where `n` is not 0, where `n` is the number of '1's in the string.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings (strings consisting of only 0-s and/or 1-s) each on a new line. The length of each binary string is between 2 and 2 * 10^5 (inclusive) and the sum of lengths of all binary strings does not exceed 2 * 10^5.
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `_` is `t`, `t` is 0, stdin is empty, and a value has been returned.

#Overall this is what the function does:Reads a specified number of binary strings from standard input, processes each string, and returns a value after processing all strings, leaving the standard input empty.

