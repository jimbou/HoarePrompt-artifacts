#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t space-separated integers (2 <= X <= 10^18).
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
        
    #State: `i` is equal to the input integer `t`, `x` is 1, `max` is either 100,000,000 or less than 100,000,000, `min` is either -100,000,000 or greater than -100,000,000, `ans` is a string containing the values of `max` and `min` in alternating order for each of the `t` input integers, `t` is the number of times the loop executed and is being printed, and the elements of the `ans` list are being printed in an unpacked manner, which are the values of `max` and `min` in alternating order for each of the `t` input integers, and `stdin` is empty.

#Overall this is what the function does:This function reads a series of integers from standard input, applies a transformation to each integer, and prints the number of steps taken for the transformation along with the transformed values. The transformation involves repeatedly dividing the integer by 2 if it's even or decrementing it by 1 if it's odd, while keeping track of the maximum and minimum values encountered during this process. The function then prints the number of steps taken for each transformation and the sequence of maximum and minimum values in alternating order.

