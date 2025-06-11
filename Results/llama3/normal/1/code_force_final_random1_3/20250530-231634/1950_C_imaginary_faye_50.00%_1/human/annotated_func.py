#State of the program right berfore the function call: stdin contains a positive integer t (1 <= t <= 1440) followed by t strings of length 5 with format hh:mm representing valid times in the 24-hour format.
    for t in range(int(input())):
        s = input()
        
        h = s[:2]
        
        if h == '00':
            print('12', end='')
        elif int(h) <= 12:
            print(h, end='')
        else:
            print('0{}'.format(int(h) - 12), end='')
        
        print(s[2:], ['AM', 'PM'][int(h) >= 12])
        
    #State: stdin is empty, s is a string of length 5 with format hh:mm representing a valid time in the 24-hour format, h is a string of length 2 representing the hour part of the time in the 24-hour format. If the hour part of the time is '00', '12' is printed. Otherwise, the hour part of the time is printed in 12-hour format if it is less than or equal to 12, otherwise it is printed in 12-hour format. and this is printed: the minutes part of the time which is s[2:] and either 'AM' or 'PM' depending on whether the hour part of the time is greater than or equal to 12 or not

#Overall this is what the function does:Converts and prints a series of 24-hour time inputs to 12-hour format, handling cases where the hour is '00', less than or equal to 12, or greater than 12, and appends 'AM' or 'PM' accordingly, ultimately emptying the standard input.

