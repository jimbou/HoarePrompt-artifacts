#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 32) followed by t strings, each of length 5 consisting of letters A and B.
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
        
    #State: `t` is an integer between 1 and 32, `l` is 0, `h` is 0, stdin is empty. The program has printed 'A' or 'B' or nothing for each of the t strings.

#Overall this is what the function does:This function reads a series of strings from standard input, each consisting of letters 'A' and 'B', and prints 'A' if the count of 'A's is greater than 'B's, 'B' if the count of 'B's is greater than 'A's, or nothing if the counts are equal, for each string. The function processes a specified number of strings, between 1 and 32, as indicated by the first integer input.

