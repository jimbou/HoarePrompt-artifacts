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
        
    #State: `t` is an integer between 1 and 32 (inclusive), `i` is `t-1`, `a` is an empty string, `l` is the number of 'A's in the last string of length 5 consisting of letters A and B, `h` is the number of 'B's in the last string of length 5 consisting of letters A and B. If `l` is greater than `h`, 'A' is printed. Otherwise, 'B' is printed.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then iterates over each string, counting the occurrences of 'A' and 'B'. If the count of 'A' is greater than the count of 'B', it prints 'A'; otherwise, it prints 'B'. The function repeats this process t times.

