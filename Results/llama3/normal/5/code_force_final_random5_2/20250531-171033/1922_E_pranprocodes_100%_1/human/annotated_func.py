#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines each containing a single integer X (2 <= X <= 10^18).
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = []
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans.append(max)
                max -= 1
                x = x // 2
            else:
                ans.append(min)
                min += 1
                x -= 1
            t += 1
        
        ans.reverse()
        
        print(t)
        
        print(*ans)
        
    #State: `x` is 1, `t` is the number of times the loop executes, `max` is 100000000 - the number of times the loop executes, `min` is -100000000 + the number of times the loop executes, `ans` is a list containing a sequence of -100000000 and 100000000 in reverse order, and `i` is the number of times the loop executes - 1, and the number of times the loop executes which is `t` is being printed, and the elements of the list `ans` which is a list containing a sequence of -100000000 and 100000000 in reverse order are being printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents a number X. For each X, the function generates a sequence of numbers by repeatedly dividing X by 2 if it's even or subtracting 1 if it's odd, and appends either 100000000 or -100000000 to a list based on whether X is even or odd. The function then prints the length of the sequence and the sequence itself in reverse order.

