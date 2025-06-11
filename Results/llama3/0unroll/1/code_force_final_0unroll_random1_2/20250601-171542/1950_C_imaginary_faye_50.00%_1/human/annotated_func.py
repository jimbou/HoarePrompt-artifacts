#State of the program right berfore the function call: stdin contains a valid input: an integer t (1 ≤ t ≤ 1440) followed by t strings, each of length 5, representing a valid time in 24-hour format (hh:mm).
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
        
    #State: stdin contains a valid input: an integer t (1 ≤ t ≤ 1440) followed by t strings, each of length 5, representing a valid time in 12-hour format (hh:mm AM/PM).

#Overall this is what the function does:Converts 24-hour time format to 12-hour time format.

