#State of the program right berfore the function call: s is a binary string (a string consisting of only 0-s and/or 1-s) of length at least 2 and at most 2 * 10^5.
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: The value of n is the number of '1's in the binary string s, and the value of ans is the sum of the lengths of all substrings of s that end with '0' and are preceded by one or more '1's. The value of s remains unchanged.
    print(ans)
    #This is printed: sum of the lengths of all substrings of s that end with '0' and are preceded by one or more '1's

#Overall this is what the function does:This function takes a binary string of length at least 2 and at most 2 * 10^5 as input, counts the number of '1's in the string, and calculates the sum of the lengths of all substrings that end with '0' and are preceded by one or more '1's. It then prints this sum, leaving the original string unchanged.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop has executed `t` times, and the function `func_1()` has been called `t` times. The state of the variables not affected by the loop head and body remains unchanged.

#Overall this is what the function does:Reads an integer t from standard input, then reads t binary strings from standard input and processes each string by calling the function func_1() t times.

