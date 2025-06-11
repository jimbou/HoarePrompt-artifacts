#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1440) and then t strings s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: day is 'AM' or 'PM', n is 0, h is an integer between 0 and 23 inclusive, m is an integer between 0 and 59 inclusive, _ is n, stdin contains 0 strings s of length 5 with format hh:mm representing a valid time in the 24-hour format. If h is 0, then day is 'AM' and h is 12. Otherwise, if h is greater than 12, then day is 'PM' and h is an integer between -12 and 11 inclusive. If h is 12, then day is 'AM'.

#Overall this is what the function does:This function takes an integer t and t strings representing times in 24-hour format as input, converts each time to 12-hour format, and prints the converted time along with 'AM' or 'PM'. The function iterates through each input time, adjusts the hour and day accordingly, and outputs the result. After processing all input times, the function concludes, leaving the input stream empty.

