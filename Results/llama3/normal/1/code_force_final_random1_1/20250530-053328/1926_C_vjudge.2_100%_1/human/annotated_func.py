#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 10^4) and then a list of integers (between 1 and 2 * 10^5).
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: Output State: `N` is 200001, `t` is an integer between 1 and 10^4, `pd` is a list of 200001 integers where each element `pd[i]` is equal to the sum of the integer values of all characters in the string `i` plus the previous element `pd[i-1]`, `i` is a string with the same number of characters as the number of iterations of the loop, `stdin` contains 1 input: a list of integers, `N` is greater than 1, `j` is the last character of the string `i`.
    #
    #In natural language, the output state after the loop executes all the iterations is that the list `pd` has been updated such that each element `pd[i]` is equal to the sum of the integer values of all characters in the string `i` plus the previous element `pd[i-1]`, and the string `i` has been fully processed. The other variables remain unchanged.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: Output State: `N` is 200001, `t` is 0, `pd` is a list of 200001 integers where each element `pd[i]` is equal to the sum of the integer values of all characters in the string `i` plus the previous element `pd[i-1]`, `i` is a string with the same number of characters as the number of iterations of the loop, `n` is an integer greater than 1 and less than 10^4, `N` is greater than 1, `j` is the last character of the string `i`, stdin contains no input, and the value of `pd[n]` which is the sum of the integer values of all characters in the string `n` plus the previous element `pd[n-1]` is being printed, and `n` is returned, `_` is `t`, and the sum of the integer values of all characters in the string `n` plus the previous element `pd[n-1]` is being printed.
    #
    #In natural language, the output state after the loop executes all the iterations is that the list `pd` has been updated such that each element `pd[i]` is equal to the sum of the integer values of all characters in the string `i` plus the previous element `pd[i-1]`, and the string `i` has been fully processed. The other variables remain unchanged.

#Overall this is what the function does:This function reads an integer `t` and a list of integers from standard input, calculates the cumulative sum of the integer values of all characters in the string representation of each integer from 1 to 200000, and then prints the cumulative sum for each of the `t` input integers.

