#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1.
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: The list s remains unchanged, n is the total number of 1's in the list s, and ans is the sum of the number of 1's in each sequence of 1's in the list s plus the number of 0's that follow each sequence of 1's.
    print(ans)
    #This is printed: the sum of the number of 1's in each sequence of 1's in the list s plus the number of 0's that follow each sequence of 1's

#Overall this is what the function does:This function calculates the sum of the number of 1's in each sequence of 1's in a given list of binary integers, plus the number of 0's that immediately follow each sequence of 1's. It takes no input parameters and returns the calculated sum, leaving the original list unchanged.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t binary strings (each consisting of only 0-s and/or 1-s) of length between 2 and 2 * 10^5
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop will execute `t` times, and each time it will call the function `func_1()`. The output state will be the result of the last execution of `func_1()`. Since the problem doesn't specify what `func_1()` does, the output state cannot be determined. However, it can be said that the output state will be the result of `t` executions of `func_1()`, with the input being the binary strings from stdin.

#Overall this is what the function does:Reads an integer t from standard input, followed by t binary strings, and executes a function func_1() t times, with the final output state being the result of the last execution of func_1().

