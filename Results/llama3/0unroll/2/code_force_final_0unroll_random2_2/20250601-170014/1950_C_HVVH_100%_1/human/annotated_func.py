#State of the program right berfore the function call: stdin contains a valid input: first an integer (1 <= t <= 1440) and then t strings of length 5 in the format hh:mm, where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
        
    #State: Output State: The loop has executed n times, printing n lines of output in the format 'hh:mm AM/PM', where 'hh' is the hour in 12-hour format and 'mm' is the minute. The day variable remains unchanged, still set to 'AM'. The stdin has been consumed, containing t strings of length 5 in the format 'hh:mm', where 'hh' is an integer from 00 to 23 and 'mm' is an integer from 00 to 59.

#Overall this is what the function does:This function reads a series of time inputs in 24-hour format from standard input, converts them to 12-hour format, and prints each time in the format 'hh:mm AM/PM'. The number of time inputs is specified by an initial integer input. The function consumes all input from standard input and produces a corresponding number of output lines, with the day indicator ('AM' or 'PM') determined by the hour of each input time.

