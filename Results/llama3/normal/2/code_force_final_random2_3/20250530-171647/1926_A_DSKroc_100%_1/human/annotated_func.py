#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 32) and then t strings of length 5 consisting of letters A and B.
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: `t` is greater than 0 and less than or equal to 32, `q` is `t-1`, `ac` is the number of 'A's in the string `s`, `bc` is the number of 'B's in the string `s`, `s` is a string of length 5 consisting of letters A and B, stdin is empty. If `ac` is greater than `bc`, 'A' is printed. Otherwise, 'B' is printed.

#Overall this is what the function does:This function reads a series of input strings from standard input, each consisting of 5 letters 'A' and 'B', and prints the dominant letter ('A' if 'A's are more than 'B's, 'B' otherwise) for each string. The function processes a specified number of strings (between 1 and 32), as indicated by the first input integer. After processing all strings, the function leaves the standard input empty.

