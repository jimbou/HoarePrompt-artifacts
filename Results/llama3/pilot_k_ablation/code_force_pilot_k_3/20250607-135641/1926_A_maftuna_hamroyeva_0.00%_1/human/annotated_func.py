#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 32) followed by t strings of length 5 consisting of letters A and B.
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
        
    #State: `t` is 0, `a` is an empty string, `i` is the initial value of `t`, `l` is the total number of 'A's in all input strings, `h` is the total number of characters in all input strings that are not 'A', stdin is empty. If `l` is greater than `h`, 'A' is printed for each iteration where `l` > `h`. If `l` is less than or equal to `h`, 'B' is printed for each iteration where `l` < `h`.

#Overall this is what the function does:This function reads a series of strings from standard input, each consisting of letters 'A' and 'B', and prints 'A' or 'B' for each string based on the majority of 'A's or 'B's. It processes a specified number of strings (t) and keeps track of the total count of 'A's and 'B's across all strings. After processing all strings, the function leaves the input stream empty and prints 'A' for strings with more 'A's and 'B' for strings with more 'B's.

