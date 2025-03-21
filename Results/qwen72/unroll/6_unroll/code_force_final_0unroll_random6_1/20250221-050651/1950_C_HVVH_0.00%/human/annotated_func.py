#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1440, and s is a string of length 5 in the format "hh:mm" where hh is an integer from 00 to 23 and mm is an integer from 00 to 59, representing a valid time in 24-hour format.
def func():
    day = 'AM'
    n = int(input())
    for _ in range(n):
        h, m = map(int, input().split(':'))
        
        if h == 0:
            h = 12
            day = 'AM'
        elif h > 12:
            h = h - 12
            day = 'PM'
        else:
            day = 'PM'
            if h == 12:
                day = 'AM'
        
        print(f'{h:02d}:{m:02d}', day)
        
    #State: The values of `t`, `s`, and `n` remain unchanged. The value of `day` will be 'PM' if the loop executes at least once and the hour `h` is not 12. If the hour `h` is 12, `day` will be 'AM'. The loop will print the time in 12-hour format followed by 'AM' or 'PM' for each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `n` from the user, representing the number of times to perform the following action: For each of the `n` iterations, it reads a time in the format "hh:mm" from the user, converts this time from 24-hour format to 12-hour format, and prints the converted time along with 'AM' or 'PM'. The final state of the program after the function concludes is that `n` and the input times remain unchanged, and the function has printed the converted times for each input.

