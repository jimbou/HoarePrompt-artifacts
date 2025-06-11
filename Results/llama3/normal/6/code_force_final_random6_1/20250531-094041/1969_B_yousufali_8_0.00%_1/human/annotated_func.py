#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers. All integers are either 0 or 1.
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `stdin` is empty, `s` is a list of integers where all integers are either 0 or 1, `i` is equal to the length of `s`, `n` is equal to the number of 1's in `s`, and `ans` is the sum of all the numbers from 2 to `n+1` where `n` is the number of 1's in `s`
    print(ans)
    #This is printed: the sum of all the numbers from 2 to n+1 (where n is the number of 1's in the list s)

#Overall this is what the function does:This function reads a space-separated list of 0s and 1s from standard input, calculates the sum of all numbers from 2 to the total count of 1s plus one, and prints the result.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing a binary string s (2 <= |s| <= 2 * 10^5; s_i in {0, 1}).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer equal to 0, stdin contains 0 lines, and a function `func_1()` has been called and returned.

#Overall this is what the function does:Reads an integer t from standard input, reads t lines of binary strings from standard input, and calls a function func_1() t times. After execution, the value of t is 0, and the standard input is empty.

