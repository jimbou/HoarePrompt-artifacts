#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 32), and the remaining t inputs are strings of length 5 consisting of letters A and B.
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
        
    #State: The output will be a sequence of 'A's and 'B's, each representing the dominant letter in the corresponding input string. The length of the output sequence will be equal to the value of `t`. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads a series of input strings from standard input, each consisting of the letters A and B, and prints the dominant letter in each string. The number of input strings is specified by the first input, an integer t. The function outputs a sequence of 'A's and 'B's, each representing the dominant letter in the corresponding input string, without modifying the original input strings or the value of t.

