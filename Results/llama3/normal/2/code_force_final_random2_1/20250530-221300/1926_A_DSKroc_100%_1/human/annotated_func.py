#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 32) followed by t strings of length 5 consisting of letters A and B.
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
        
    #State: t is an integer between 1 and 32, q is t-1, ac is 0, bc is 0, s is an empty string, stdin is empty. If the number of 'A's is greater than the number of 'B's in each of the t strings, 'A' is printed t times. Otherwise, 'B' is printed t times.

#Overall this is what the function does:This function reads a series of strings from standard input, each consisting of the letters 'A' and 'B', and prints 'A' or 'B' for each string depending on which letter appears more frequently. It processes a specified number of strings, as indicated by an initial integer input, and outputs the dominant letter for each string.

