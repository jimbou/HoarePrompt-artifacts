#State of the program right berfore the function call: s is a string consisting of only 0-s and/or 1-s.
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: Output State: The string s remains unchanged, n is the total number of '1's in the string s, and ans is the total number of '0's in the string s that are preceded by at least one '1'.
    print(ans)
    #This is printed: the total number of '0's in the string s that are preceded by at least one '1'

#Overall this is what the function does:The function takes a string of binary digits (0s and 1s) as input, counts the total number of '0's that are preceded by at least one '1', and returns this count. The input string remains unchanged.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5; s_i in {0, 1}).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop has executed t times, and the function func_1() has been called t times. The state of the variables in the loop head and body has been updated accordingly. The state of the other variables in the precondition remains unchanged.

#Overall this is what the function does:Reads an integer t from standard input, then reads t binary strings from standard input and processes each string by calling the function func_1() t times.

