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
        
    #State: t is greater than or equal to 0, i is t, a is an empty string, stdin is empty, l is the sum of the number of 'A's in all strings, h is the sum of the number of 'B's in all strings. If l is greater than h, 'A' has been printed t times. Otherwise, 'B' has been printed t times.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t strings of length 5 consisting of letters A and B. It then iterates over each string, counting the occurrences of 'A' and 'B'. If the count of 'A's is greater than the count of 'B's, it prints 'A' t times. Otherwise, it prints 'B' t times. The function does not return any value, but it modifies the standard input by consuming the input strings and prints the result to the standard output.

