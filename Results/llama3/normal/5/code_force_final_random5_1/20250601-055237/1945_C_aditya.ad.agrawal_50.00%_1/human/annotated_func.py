#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (3 <= n <= 3*10^5) and then a string a of length n, consisting only of 0 and 1.
    t = int(input())
    while t:
        n = int(input())
        
        input_string = input()
        
        arr = [int(ch) for ch in input_string]
        
        z = arr.count(0)
        
        o = arr.count(1)
        
        z_r = z
        
        o_r = o
        
        z_l = 0
        
        o_l = 0
        
        dist, ans, pos = abs(n / 2), 0, 0
        
        if o_r >= (z_r + o_r) / 2:
            b_d = dist
        else:
            b_d = 30001
        
        for i in arr:
            pos += 1
            if i == 0:
                z_l += 1
                z_r -= 1
            else:
                o_l += 1
                o_r -= 1
            if o_r >= (z_r + o_r) / 2 and z_l >= (z_l + o_l) / 2 and b_d > abs(n / 
                2 - pos):
                ans = pos
                b_d = abs(n / 2 - pos)
        
        print(ans)
        
        t -= 1
        
    #State: t is 0, stdin contains no test cases, n is an integer, input_string is a string of length n consisting only of 0 and 1, arr is a list of integers, z is the number of zeros in arr, o is the number of ones in arr, z_r is 0, o_r is 0, z_l is the number of zeros in arr, o_l is the number of ones in arr, dist is the absolute value of n/2, ans is the position where the condition o_r >= (z_r + o_r) / 2 and z_l >= (z_l + o_l) / 2 and b_d > abs(n / 2 - pos) is first met, pos is n, and b_d is the absolute value of n/2 minus the position where the condition o_r >= (z_r + o_r) / 2 and z_l >= (z_l + o_l) / 2 and b_d > abs(n / 2 - pos) is first met, and the position where the condition o_r >= (z_r + o_r) / 2 and z_l >= (z_l + o_l) / 2 and b_d > abs(n / 2 - pos) is first met which is ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a string a of length n containing only 0s and 1s. It then finds the position in the string where the number of 1s to the right of the position is greater than or equal to half of the remaining characters, and the number of 0s to the left of the position is greater than or equal to half of the characters to the left. If such a position exists, it prints the position; otherwise, it prints 0. The function continues this process until all test cases have been read from standard input.

