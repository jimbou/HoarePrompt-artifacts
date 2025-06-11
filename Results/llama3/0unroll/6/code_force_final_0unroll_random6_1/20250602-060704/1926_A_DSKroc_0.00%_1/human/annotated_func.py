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
        
    #State: The loop has executed `t` iterations, where in each iteration, it has read a string of length 5 from stdin, counted the occurrences of 'A' and 'B' in the string, and stored the counts in variables `ac` and `bc` respectively. The values of `ac` and `bc` are reset to 0 at the beginning of each iteration. The final values of `ac` and `bc` are the counts of 'A' and 'B' in the last string read from stdin. The value of `t` remains unchanged.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: *The loop has executed `t` iterations, where in each iteration, it has read a string of length 5 from stdin, counted the occurrences of 'A' and 'B' in the string, and stored the counts in variables `ac` and `bc` respectively. The values of `ac` and `bc` are reset to 0 at the beginning of each iteration. The final values of `ac` and `bc` are the counts of 'A' and 'B' in the last string read from stdin. The value of `t` remains unchanged. If the count of 'A' is greater than the count of 'B' in the last string read from stdin, 'A' is printed. Otherwise, 'B' is printed.

#Overall this is what the function does:This function reads a specified number of strings from standard input, each consisting of 5 characters 'A' or 'B', counts the occurrences of 'A' and 'B' in each string, and prints 'A' if 'A' occurs more frequently than 'B' in the last string, otherwise prints 'B'.

