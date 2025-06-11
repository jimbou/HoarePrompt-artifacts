#State of the program right berfore the function call: stdin contains a single integer t (1 <= t <= 1440) followed by t strings, each of length 5, representing a valid time in 24-hour format (hh:mm).
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
        
    #State: Output State: day is 'AM', n is 0, stdin is empty.

#Overall this is what the function does:This function reads a series of time inputs in 24-hour format from standard input, converts them to 12-hour format, and prints each time in the format 'hh:mm' followed by 'AM' or 'PM', depending on the time of day. It processes a specified number of time inputs, as indicated by an initial integer input, and leaves the standard input empty after processing all inputs.

