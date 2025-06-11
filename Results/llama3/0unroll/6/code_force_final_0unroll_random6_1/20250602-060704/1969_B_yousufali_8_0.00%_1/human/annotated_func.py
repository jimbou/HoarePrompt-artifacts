#State of the program right berfore the function call: stdin contains one input: a space-separated list of integers. The list contains only 0s and 1s.
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: s is a list of integers containing only 0s and 1s, n is the number of 1s in s, ans is the sum of the lengths of all the sublists of consecutive 1s in s plus the number of 1s in s, stdin is empty
    print(ans)
    #This is printed: the sum of the lengths of all the sublists of consecutive 1s in s plus the number of 1s in s

#Overall this is what the function does:The function reads a space-separated list of 0s and 1s from standard input, calculates the sum of the lengths of all sublists of consecutive 1s plus the total number of 1s, and prints the result. The function does not modify the input list or any external state, and it consumes the entire input from standard input.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than or equal to 1).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` is an integer greater than or equal to 1, stdin contains no input.

#Overall this is what the function does:Reads an integer from standard input, calls a function named `func_1` that many times, and leaves the standard input empty.

