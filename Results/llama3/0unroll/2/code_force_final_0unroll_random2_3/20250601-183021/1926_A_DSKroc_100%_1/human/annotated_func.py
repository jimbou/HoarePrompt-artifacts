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
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: The loop will print 'A' or 'B' t times, where 'A' is printed if the number of 'A's in the corresponding string is greater than the number of 'B's, and 'B' is printed otherwise. The value of t remains unchanged.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then prints 'A' or 'B' t times, where 'A' is printed if the number of 'A's in the corresponding string is greater than the number of 'B's, and 'B' is printed otherwise. The function does not return any value or modify the input variables, but rather produces output based on the input strings.

