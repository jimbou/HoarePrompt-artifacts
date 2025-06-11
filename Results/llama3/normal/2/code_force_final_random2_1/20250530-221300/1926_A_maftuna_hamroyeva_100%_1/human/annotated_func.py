#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 32) followed by t strings of length 5 consisting of letters A and B.
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: `t` is 0, `i` is `t`, `a` is an empty string, `stdin` is empty, `l` is the total number of 'A's in all strings, and `h` is the total number of 'B's in all strings. The output will be a sequence of 'A's and 'B's, where 'A' is printed if the total number of 'A's in the corresponding string is greater than the total number of 'B's, and 'B' is printed otherwise.

#Overall this is what the function does:This function reads a sequence of strings from standard input, where each string consists of letters 'A' and 'B', and prints a sequence of 'A's and 'B's indicating whether the number of 'A's is greater than the number of 'B's in each string. The function processes a specified number of strings, as indicated by an initial integer input, and prints the results in the same order as the input strings.

