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
        
    #State: stdin contains no inputs, and the stdout contains t strings of length 7 with format hh:mm AM/PM representing a valid time in the 12-hour format.

#Overall this is what the function does:Converts 24-hour time format to 12-hour time format for a given number of inputs. It takes an integer t (1 <= t <= 1440) and t strings of length 5 representing valid times in 24-hour format, and outputs t strings of length 7 in 12-hour format with AM/PM suffix.

