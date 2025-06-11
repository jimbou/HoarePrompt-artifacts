#State of the program right berfore the function call: stdin contains a valid input: first an integer (1 <= t <= 1440) and then t strings of length 5 in the format hh:mm, where hh is an integer from 00 to 23 and mm is an integer from 00 to 59.
    for _ in range(int(input())):
        h, m = map(str, input().split(':'))
        
        h1, m1 = '', m
        
        time = ''
        
        if h == '01':
            h1 = '01'
            time = 'AM'
        elif h == '02':
            h1 = '02'
            time = 'AM'
        elif h == '03':
            h1 = '03'
            time = 'AM'
        elif h == '04':
            h1 = '04'
            time = 'AM'
        elif h == '05':
            h1 = '05'
            time = 'AM'
        elif h == '06':
            h1 = '06'
            time = 'AM'
        elif h == '07':
            h1 = '07'
            time = 'AM'
        elif h == '08':
            h1 = '08'
            time = 'AM'
        elif h == '09':
            h1 = '09'
            time = 'AM'
        elif h == '10':
            h1 = '10'
            time = 'AM'
        elif h == '11':
            h1 = '11'
            time = 'AM'
        elif h == '12':
            h1 = '12'
            time = 'AM'
        elif h == '13':
            h1 = '01'
            time = 'PM'
        elif h == '14':
            h1 = '02'
            time = 'PM'
        elif h == '15':
            h1 = '03'
            time = 'PM'
        elif h == '16':
            h1 = '04'
            time = 'PM'
        elif h == '17':
            h1 = '05'
            time = 'PM'
        elif h == '18':
            h1 = '06'
            time = 'PM'
        elif h == '19':
            h1 = '07'
            time = 'PM'
        elif h == '20':
            h1 = '08'
            time = 'PM'
        elif h == '21':
            h1 = '09'
            time = 'PM'
        elif h == '22':
            h1 = '10'
            time = 'PM'
        elif h == '23':
            h1 = '11'
            time = 'PM'
        elif h == '00':
            h1 = '12'
            time = 'PM'
        
        print(h1, ':', m, ' ', time, sep='')
        
    #State: The output state will be a series of time conversions from 24-hour format to 12-hour format with AM/PM indicator. The number of lines in the output will be equal to the initial integer input. Each line will contain a time in the format hh:mm AM/PM, where hh is an integer from 01 to 12 and mm is an integer from 00 to 59.

#Overall this is what the function does:Converts a series of 24-hour time inputs to 12-hour format with AM/PM indicator and prints the results. The function takes no parameters and returns no value, instead printing the converted times directly. It processes a variable number of input times, as specified by an initial integer input, and outputs the same number of converted times.

