#State of the program right berfore the function call: stdin contains a single integer t (1 ≤ t ≤ 1440) followed by t strings, each of length 5, in the format hh:mm, representing a valid time in the 24-hour format.
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
        
    #State: h is a string representing the hour part of the input time, m is the minute part of the input time, m1 is the minute part of the input time, stdin is empty. If h is '01', then h1 is '01' and time is 'AM'. If h is '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', or '12', then h1 is the same as h and time is 'AM'. If h is '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', or '00', then h1 is '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', or '12' respectively and time is 'PM'; otherwise, h1 and time remain unchanged. The time in 12-hour format is printed, where h1 is the hour part, m is the minute part, and time is 'AM' or 'PM' depending on the hour part.

#Overall this is what the function does:Converts 24-hour time to 12-hour time format. Accepts a single integer t (1 ≤ t ≤ 1440) followed by t strings, each of length 5, in the format hh:mm, representing a valid time in the 24-hour format. For each input time, it converts the hour part to 12-hour format, determines whether the time is AM or PM, and prints the time in 12-hour format (hh:mm AM/PM). The function does not return any value but prints the converted time for each input.

