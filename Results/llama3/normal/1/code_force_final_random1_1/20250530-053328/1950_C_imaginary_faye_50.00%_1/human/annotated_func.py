#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1440) and then t strings s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: t is 0, s is a string of length 5 with format hh:mm representing a valid time in the 24-hour format, h is a 2-digit string representing the hour part of the input time, stdin contains no input.

#Overall this is what the function does:Converts 24-hour time format to 12-hour time format for multiple input times.

