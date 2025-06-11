#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1440) followed by t strings, each representing a valid time in 24-hour format (hh:mm).
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
            day = 'AM'
            if h == 12:
                day = 'PM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: Output State: day is 'AM', n is 0, stdin contains no strings.

#Overall this is what the function does:This function reads a series of time inputs in 24-hour format from standard input, converts each time to 12-hour format, and prints the converted time along with the day period ('AM' or 'PM'). The function processes a specified number of time inputs, as indicated by the first input value, and does not return any value.

