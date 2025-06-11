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
        
    #State: Output State: The variable `ac` and `bc` will have been reset to 0 for each iteration of the loop, and the variable `s` will have taken on the value of each of the `t` strings from stdin in succession. The variable `t` will remain unchanged.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: *The variables `ac` and `bc` have been reset to 0 for each iteration of the loop, and the variable `s` has taken on the value of each of the `t` strings from stdin in succession. The variable `t` remains unchanged. If `ac` is greater than `bc`, 'A' is printed. Otherwise, if `ac` is less than or equal to `bc`, 'B' is printed.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then iterates over each string, counting the occurrences of 'A' and 'B'. If the count of 'A' is greater than the count of 'B', it prints 'A'; otherwise, it prints 'B'. This process is repeated for each of the t strings.

