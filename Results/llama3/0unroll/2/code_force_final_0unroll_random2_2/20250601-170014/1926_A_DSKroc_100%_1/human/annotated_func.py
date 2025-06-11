#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 32) and then t strings of length 5 consisting of letters A and B.
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
        
    #State: The output will be a sequence of 'A's and 'B's, each representing the majority character in the corresponding input string. The number of 'A's and 'B's will be equal to the value of `t`. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads an integer `t` from standard input, followed by `t` strings of length 5 consisting of letters A and B. It then determines the majority character in each string and prints the corresponding character ('A' or 'B') for each string. The function outputs a sequence of `t` characters, where each character represents the majority character in the corresponding input string.

