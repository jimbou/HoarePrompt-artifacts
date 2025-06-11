#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1440) and then t strings s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: h is a string representing the hour of the tth time input in 24-hour format, m is a string representing the minute of the tth time input, m1 is the minute of the tth time input, stdin is empty, t is 0. If h is '01', then h1 is '01' and time is 'AM'. If h is '02', '03', '04', '05', '06', '07', '08', '09', '10', or '11', then h1 is '02', '03', '04', '05', '06', '07', '08', '09', '10', or '11' respectively and time is 'AM'. If h is '12', then h1 is '12' and time is 'PM'. If h is '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', or '23', then h1 is '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', or '11' respectively and time is 'PM'. If h is '00', then h1 is '12' and time is 'AM', and the time in 12-hour format is printed as h1 : m time.

#Overall this is what the function does:Converts and prints 24-hour time inputs to 12-hour format.

