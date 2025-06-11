#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 32) followed by t strings of length 5 consisting of letters A and B.
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
        
    #State: t is an integer between 1 and 32, q is t-1, ac is the sum of the number of 'A's in all strings s, bc is the sum of the number of 'B's in all strings s, s is an empty string, stdin contains 0 strings of length 5 consisting of letters A and B.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: *t is an integer between 1 and 32, q is t-1, ac is the sum of the number of 'A's in all strings s, bc is the sum of the number of 'B's in all strings s, s is an empty string, stdin contains 0 strings of length 5 consisting of letters A and B. If ac is higher than bc, 'A' is printed. If ac is less than or equal to bc, 'B' is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, counts the occurrences of 'A' and 'B' in each string, and prints 'A' if the total count of 'A's is higher than the total count of 'B's, otherwise it prints 'B'.

