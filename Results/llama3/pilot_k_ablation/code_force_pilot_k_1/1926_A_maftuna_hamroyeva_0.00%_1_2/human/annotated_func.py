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
        
    #State: `t` is 0, `l` is 0, `h` is 0, `i` is `t` (initial value), stdin is empty.

#Overall this is what the function does:This function reads a specified number of strings from standard input, each consisting of letters 'A' and 'B', and prints the dominant letter ('A' or 'B') for each string. After processing all strings, the function leaves the input stream empty and resets its internal counters.

