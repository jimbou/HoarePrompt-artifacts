#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1440, and for each of the t test cases, there is a string s of length 5 with the format "hh:mm", where hh is an integer from 00 to 23 representing the hour, and mm is an integer from 00 to 59 representing the minute. The input will always be a valid time in 24-hour format.
def func():
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
        
    #State: a series of printed lines, each in the format "h1:m time" corresponding to each of the t test cases converted from 24-hour to 12-hour format with AM/PM notation.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads a time in 24-hour format "hh:mm". It then prints the time converted to 12-hour format with AM/PM notation.

