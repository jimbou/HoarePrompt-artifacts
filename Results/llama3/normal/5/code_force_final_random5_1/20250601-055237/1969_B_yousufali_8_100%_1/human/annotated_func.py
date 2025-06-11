#State of the program right berfore the function call: s is a binary string (a string consisting of only 0-s and/or 1-s) of length at least 2 and at most 2 * 10^5.
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is a binary string of length at least 2 and at most 2 * 10^5, `i` is equal to the length of `s`, `ans` is the total number of '1's in `s` plus the number of '0's in `s` that are preceded by at least one '1', and `n` is equal to the number of '1's in the suffix of `s` that ends at the last '1' in `s`.
    print(ans)
    #This is printed: the total number of '1's in the binary string s plus the number of '0's in s that are preceded by at least one '1'

#Overall this is what the function does:This function takes a binary string of length at least 2 and at most 2 * 10^5 as input, and returns the total number of '1's in the string plus the number of '0's that are preceded by at least one '1'.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than or equal to 1).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer greater than or equal to 1, `_` is `t-1`, and the function `func_1()` has been executed.

#Overall this is what the function does:Reads an integer from standard input, executes the function `func_1()` that many times, and then concludes without returning any value.

