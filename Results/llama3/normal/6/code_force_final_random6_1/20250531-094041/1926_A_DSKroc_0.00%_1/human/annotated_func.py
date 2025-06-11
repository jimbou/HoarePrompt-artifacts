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
        
    #State: `t` is an integer between 1 and 32 (inclusive), `q` is `t-1`, `ac` is the number of 'A's in `s`, `bc` is the number of 'B's in `s`, `s` is a string of length 5 consisting of letters A and B, `stdin` is empty.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: *`t` is an integer between 1 and 32 (inclusive), `q` is `t-1`, `ac` is the number of 'A's in `s`, `bc` is the number of 'B's in `s`, `s` is a string of length 5 consisting of letters A and B, `stdin` is empty. If `ac` is greater than `bc`, 'A' is printed. Otherwise, 'B' is printed.

#Overall this is what the function does:This function reads a series of strings from standard input, each consisting of 5 characters 'A' or 'B', and prints 'A' if the number of 'A's in the string is greater than the number of 'B's, otherwise it prints 'B'. The function processes multiple strings as specified by an initial integer input, which ranges from 1 to 32.

