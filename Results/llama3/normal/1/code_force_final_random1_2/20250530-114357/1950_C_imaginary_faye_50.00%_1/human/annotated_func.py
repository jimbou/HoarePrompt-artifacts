#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1440) followed by t strings, each representing a valid time in 24-hour format (hh:mm).
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
        
    #State: stdin is empty, s is the last string, h is the hour part of the last string. If the hour part of the last string is '00', '12' is printed. Otherwise, if the hour part of the last string is less than or equal to 12, the hour part of the last string is printed. Otherwise, the hour part of the last string minus 12 is printed, prefixed with '0'. The code prints the minute part of the last string (s[2:]) and either 'AM' or 'PM' depending on whether the hour part of the last string is greater than or equal to 12 or not.

#Overall this is what the function does:Converts 24-hour time format to 12-hour time format for a given number of input times. For each input time, it prints the hour in 12-hour format (01-12), followed by the minutes, and either 'AM' or 'PM' depending on the hour. If the input hour is 00, it prints 12. If the input hour is greater than 12, it subtracts 12 from the hour and prints the result, prefixed with '0' if necessary.

