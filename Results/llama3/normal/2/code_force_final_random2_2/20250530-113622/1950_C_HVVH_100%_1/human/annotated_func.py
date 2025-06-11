#State of the program right berfore the function call: stdin contains a valid input: first an integer (1 <= integer <= 1440) and then a string of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: day is either 'AM' or 'PM', n is 0, stdin is empty, _ is n.

#Overall this is what the function does:This function reads a series of time inputs from the user, converts them to 12-hour format, and prints them along with their respective AM/PM designations. It processes a specified number of inputs, determined by the first integer input, and then terminates, leaving the standard input empty.

