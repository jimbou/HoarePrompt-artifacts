#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers. The list contains only 0s and 1s.
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: s is a list of integers containing only 0s and 1s, n is the number of 1s in s, ans is the sum of the lengths of all sequences of 1s in s plus the number of 1s in s, stdin is empty.
    print(ans)
    #This is printed: the sum of the lengths of all sequences of 1s in s plus the number of 1s in s

#Overall this is what the function does:This function reads a space-separated list of 0s and 1s from standard input, calculates the sum of the lengths of all sequences of 1s plus the total number of 1s, and prints the result.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5; s_i in {0, 1}).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is 0, stdin is empty.

#Overall this is what the function does:Reads a specified number of binary strings from standard input and processes each one, leaving the input stream empty.

