#State of the program right berfore the function call: stdin contains a valid input: the first line contains a single integer t (1 <= t <= 1440), and the following t lines each contain a string s of length 5 with format hh:mm representing a valid time in the 24-hour format.
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
        
    #State: The output contains t lines, each representing a time in 12-hour format. For each time, if the hour is 0, it is replaced with 12. If the hour is less than or equal to 12, it remains the same. If the hour is greater than 12, it is subtracted by 12 and a leading 0 is added if necessary. The minute remains the same. 'AM' is appended if the hour is less than 12, and 'PM' is appended otherwise.

#Overall this is what the function does:Converts a series of 24-hour times to 12-hour format and prints them. For each time, if the hour is 0, it is replaced with 12. If the hour is less than or equal to 12, it remains the same. If the hour is greater than 12, it is subtracted by 12 and a leading 0 is added if necessary. The minute remains the same. 'AM' is appended if the hour is less than 12, and 'PM' is appended otherwise.

