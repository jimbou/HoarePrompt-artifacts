#State of the program right berfore the function call: stdin contains a valid input: the first line contains a single integer t (1 <= t <= 1440), and the following t lines each contain a string s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: h is an empty string, m1 is a string of two digits representing minutes equal to m, stdin is empty, t is 0, and m is a string of two digits representing minutes. If the initial value of h is '01', then time is 'AM' and h1 is '01'. If the initial value of h is '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', or '12', then time is 'AM' and h1 is '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', or '12' respectively. If the initial value of h is '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', or '00', then time is 'PM' and h1 is '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', or '12' respectively, and the time in the format h1:m:time has been printed for all input times.

#Overall this is what the function does:Converts 24-hour time format to 12-hour time format and prints the converted time for each input time.

