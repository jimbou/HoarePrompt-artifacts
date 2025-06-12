#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing an integer X (2 <= X <= 10^18).
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = ''
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        
        print(t)
        
        print(*ans)
        
    #State: `i` is equal to the initial value of `t`, `x` is 1, `t` is the number of times the while loop executed in the last iteration, `stdin` is empty, `ans` is a string containing the values of `max` and `min` in alternating order, with the values of `max` decreasing by 1 and the values of `min` increasing by 1, `max` is the original value of `max` minus the total number of times `x` was even in all iterations, `min` is the original value of `min` plus the total number of times `x` was odd in all iterations. If the initial value of `t` is 0, the loop does not execute and `i` is 0, `x` is not defined, `t` is 0, `stdin` contains the initial two inputs, `ans` is an empty string, `max` is 100000000, and `min` is -100000000.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers to process. For each integer X, it generates a sequence of alternating maximum and minimum values, starting from 100000000 and -100000000 respectively, and decreasing/increasing by 1 for each iteration. The sequence is constructed by repeatedly dividing X by 2 if it's even, or subtracting 1 if it's odd, until X becomes 1. The function then prints the length of the sequence and the sequence itself. If the initial value of t is 0, the function does not process any integers and leaves the input unchanged.

