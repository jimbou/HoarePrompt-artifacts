#State of the program right berfore the function call: stdin contains a positive integer t (1 <= t <= 1440) followed by t strings, each representing a valid time in 24-hour format (hh:mm).
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
        
    #State: Output State: day is 'AM', n is 0, stdin contains no strings.

#Overall this is what the function does:This function reads a positive integer t from standard input, followed by t strings representing times in 24-hour format. It then converts each time to 12-hour format and prints the converted time along with 'AM' or 'PM'. The function iterates through all input times, performing the conversion and printing the result for each one. After processing all input times, the function concludes, leaving the input stream empty.

