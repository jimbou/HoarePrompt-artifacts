#State of the program right berfore the function call: s is a list of integers containing only 0s and 1s.
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `s` is a list of integers containing only 0s and 1s, `i` is `len(s) - 1`, `n` is the total number of 1s in `s`, `ans` is the sum of the lengths of all sequences of 1s in `s` plus the number of 0s that follow a sequence of 1s.
    print(ans)
    #This is printed: the sum of the lengths of all sequences of 1s in the list s plus the number of 0s that follow a sequence of 1s

#Overall this is what the function does:This function calculates and prints the sum of the lengths of all sequences of 1s in a given list of binary integers plus the number of 0s that immediately follow a sequence of 1s. It takes a list of binary integers as input, counts the total number of 1s and the number of 0s that follow a sequence of 1s, and returns the total sum of these counts.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer greater than 0, `_` is `t-1`, and a function `func_1()` has been called and executed.

#Overall this is what the function does:Reads an integer from standard input, representing the number of times to execute a function named `func_1`, and then calls `func_1` that many times.

