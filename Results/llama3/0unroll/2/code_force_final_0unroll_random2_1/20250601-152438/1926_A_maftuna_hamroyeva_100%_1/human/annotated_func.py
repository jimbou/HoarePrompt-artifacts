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
        
    #State: The output will be a sequence of t lines, each containing either 'A' or 'B', depending on whether the count of 'A's is greater than the count of 'B's in the corresponding input string. The value of t remains unchanged, and the input strings are consumed from stdin.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then outputs a sequence of t lines, each containing either 'A' or 'B', depending on whether the count of 'A's is greater than the count of 'B's in the corresponding input string. The function does not modify the input strings or the value of t, and it consumes the input strings from standard input.

