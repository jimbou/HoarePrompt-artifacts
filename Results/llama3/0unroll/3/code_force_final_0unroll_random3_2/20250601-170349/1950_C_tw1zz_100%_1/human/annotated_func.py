#State of the program right berfore the function call: stdin contains a valid input: the first line contains an integer t (1 ≤ t ≤ 1440), followed by t lines each containing a string s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
            time = 'PM'
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
            time = 'AM'
        
        print(h1, ':', m, ' ', time, sep='')
        
    #State: The output state contains the same number of lines as the input, but each time is converted to 12-hour format with AM/PM suffix.

#Overall this is what the function does:This function reads a series of times in 24-hour format from standard input, converts each time to 12-hour format with AM/PM suffix, and prints the converted times. It processes multiple lines of input, where the first line specifies the number of times to follow, and each subsequent line contains a time in the format hh:mm. The function handles all possible hour values from 00 to 23, converting them to the corresponding 12-hour format with the correct AM/PM designation.

