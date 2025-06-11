#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 ≤ t ≤ 32) and then t strings of length 5 consisting of letters A and B.
    t = int(input())
    l = 0
    h = 0
    for i in range(t):
        a = str(input())
        
        for j in a:
            if j in 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        elif l < h:
            print('B')
        
    #State: `t` is an integer between 1 and 32 inclusive, `i` is `t-1`, `a` is an empty string, `l` and `h` are integers between 0 and 5t inclusive, stdin is empty. If `l` is greater than `h`, then 'A' has been printed `t` times. If `l` is less than `h`, then 'B' has been printed `t` times. If `l` is equal to `h`, then no additional action has been taken.

#Overall this is what the function does:The function reads a series of strings from standard input, each consisting of letters A and B, and prints 'A' if the count of A's is greater than the count of B's, 'B' if the count of B's is greater than the count of A's, or takes no additional action if the counts are equal. The function processes a specified number of strings, ranging from 1 to 32, and consumes all input from standard input.

