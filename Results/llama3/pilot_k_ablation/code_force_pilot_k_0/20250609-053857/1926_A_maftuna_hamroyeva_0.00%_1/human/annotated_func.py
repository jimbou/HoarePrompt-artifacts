#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 32) followed by t strings of length 5 consisting of letters A and B.
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
        
    #State: Output State: t is an integer between 1 and 32, l is 0, h is 0, stdin is empty, and the standard output contains t lines, each of which is either 'A' or 'B'.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then prints t lines to standard output, where each line is either 'A' or 'B', depending on whether the count of 'A's is greater than or less than the count of 'B's in the corresponding input string. The function does not return any value, and it leaves the standard input empty.

