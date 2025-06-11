#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1440) followed by t strings of length 5 with format hh:mm representing a valid time in the 24-hour format.
    day = 'AM'
    n = int(input())
    for _ in range(n):
        h, m = map(int, input().split(':'))
        
        if h == 0:
            h = 12
            day = 'AM'
        elif h > 12:
            h = h - 12
            day = 'PM'
        else:
            day = 'PM'
            if h == 12:
                day = 'AM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: Output State: The day is 'PM', n is 0, stdin is empty.

#Overall this is what the function does:This function reads a series of time inputs in 24-hour format from standard input, converts each time to 12-hour format, and prints the converted time along with the day period ('AM' or 'PM'). It continues this process until all input times have been processed, ultimately emptying the standard input.

