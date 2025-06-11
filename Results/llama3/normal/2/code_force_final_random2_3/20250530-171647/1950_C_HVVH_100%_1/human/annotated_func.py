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
            day = 'AM'
            if h == 12:
                day = 'PM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: day is 'AM' if h is not 12, otherwise day is 'PM'. If h is 0, h is set to 12. If h is greater than 12, h is decreased by 12. n is 0, m is an integer between 0 and 59 inclusive, _ is n, stdin contains 0 strings s of length 5 with format hh:mm representing a valid time in the 24-hour format, h is an integer between 0 and 23 inclusive, m is an integer between 0 and 59 inclusive, the time in 12-hour format, with hours ranging from 01 to 12, minutes ranging from 00 to 59, and either 'AM' or 'PM' depending on the hour, for example, 07:05 AM or 07:05 PM has been printed n times.

#Overall this is what the function does:This function takes an integer t and t strings representing times in 24-hour format as input, converts each time to 12-hour format, and prints the converted times. The function iterates t times, reading a time in 24-hour format, converting it to 12-hour format by adjusting the hour and determining whether it's AM or PM, and then printing the converted time. After processing all t times, the function concludes, having printed t times in 12-hour format.

