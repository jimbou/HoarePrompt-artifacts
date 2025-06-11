#State of the program right berfore the function call: stdin contains a valid input: the first line contains a single integer t (1 <= t <= 1440), and each of the next t lines contains a string s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: h is a string representing the hours from the input time, m1 is the minutes from the input time, m is the minutes from the input time, stdin is empty, _ is t. If h is '01', then h1 is '01' and time is 'AM'. If h is '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', or '12', then h1 is the same as h and time is 'AM' if h is '12' then time is 'PM'. If h is '00', then h1 is '12' and time is 'AM'. If h is '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', or '23', then h1 is '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', or '11' respectively and time is 'PM'. The time in 12-hour format is printed, where the hour is represented by h1, the minutes are represented by m, and the time of day is represented by time.

#Overall this is what the function does:Converts 24-hour time to 12-hour time and prints the result. The function takes no parameters and returns no value. It reads a number of test cases from standard input, then for each test case, it reads a time in 24-hour format (hh:mm), converts it to 12-hour format, and prints the result. The conversion is done by adjusting the hour and adding 'AM' or 'PM' based on the original hour. The function consumes all input and leaves the standard input empty.

