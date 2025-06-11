#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the values of X).
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
        
    #State: `x` is 1, `max` is 99999997, `min` is -99999999, `ans` is a list containing either -100000000, 100000000, -99999999, 99999999, -99999998, or 99999998 in reverse order, `t` is a positive integer greater than or equal to 3, `i` is equal to the number of test cases, stdin contains no inputs, and the value of `t` which is a positive integer greater than or equal to 3 is being printed, and the elements of the list `ans` are being printed in the order they appear in the list, which are either -100000000, 100000000, -99999999, 99999999, -99999998, or 99999998.

#Overall this is what the function does:This function reads a sequence of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents a value X. For each X, the function generates a list of integers by repeatedly dividing X by 2 if it's even, or decrementing X by 1 if it's odd, and appending either the maximum possible integer (initially 100000000) or the minimum possible integer (initially -100000000) to the list, depending on whether X is even or odd. The function then prints the length of the list and the list itself in reverse order. The function repeats this process for each test case.

