#State of the program right berfore the function call: stdin contains a positive integer t (1 <= t <= 1440) followed by t strings, each of length 5, representing valid times in 24-hour format (hh:mm), where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
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
        
    #State: day is 'AM', n is 0, stdin contains no input.

#Overall this is what the function does:The function reads a positive integer t from standard input, representing the number of time conversions to perform. It then reads t strings, each representing a time in 24-hour format (hh:mm), and for each time, it converts the hour to 12-hour format and determines whether it is AM or PM. The function prints each converted time in the format hh:mm AM/PM. After processing all input times, the function leaves the day in the state 'AM' and the input count n in the state 0, with no remaining input in standard input.

