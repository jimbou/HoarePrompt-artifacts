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
        
    #State: The output will be a series of 'A's and 'B's, each representing the dominant character in the corresponding input string. The number of lines in the output will be equal to the value of `t`.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then determines the dominant character in each string (either A or B) and prints the dominant character for each string, resulting in a series of 'A's and 'B's as output, with the number of lines equal to the value of t.

