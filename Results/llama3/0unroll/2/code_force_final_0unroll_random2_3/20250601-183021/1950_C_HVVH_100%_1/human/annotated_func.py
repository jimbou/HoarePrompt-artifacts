#State of the program right berfore the function call: stdin contains a single integer t (1 ≤ t ≤ 1440) followed by t strings, each of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: day is 'AM', n is 0, stdin is empty.

#Overall this is what the function does:This function reads a series of time inputs in 24-hour format from standard input, converts each time to 12-hour format, and prints the converted time along with the corresponding day period (AM/PM). The function processes a variable number of time inputs, as specified by an initial integer input, and continues until all inputs have been processed, leaving the standard input empty.

