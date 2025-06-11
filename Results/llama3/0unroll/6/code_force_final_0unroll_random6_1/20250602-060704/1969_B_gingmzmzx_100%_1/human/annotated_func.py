#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a binary string (a string consisting of only 0-s and/or 1-s). The integer is a positive integer and the length of the binary string is between 2 and 2 * 10^5 (inclusive).
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        
        zeroes = s.count(0)
        
        cnt = [0, 0]
        
        ans = 0
        
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += zeroes - cnt[0]
        
        print(ans)
        
    #State: The output state after the loop executes all the iterations is that the variable `n` remains unchanged as a positive integer, and the stdin is empty since all the inputs have been read and processed. The loop has printed `n` lines of output, each containing a single integer value representing the count of operations required to make all the bits in the input binary string equal. The values of other variables in the precondition remain unchanged.

#Overall this is what the function does:This function reads a positive integer `n` from standard input, followed by `n` binary strings. For each binary string, it calculates and prints the minimum number of operations required to make all bits equal. The function does not modify the input values or the state of the program, except for consuming the input and printing the results. The output consists of `n` lines, each containing a single integer representing the count of operations required for the corresponding binary string.

