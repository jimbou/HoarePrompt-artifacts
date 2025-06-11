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
        
    #State: Output State: `t` is 0, stdin contains no test cases, `n` is an integer between 3 and 3*10^5, `input_string` is a string of length `n` consisting only of 0 and 1, `arr` is a list of `n` integers (0 or 1) that must have at least `n` elements, `z` is the number of 0's in `arr`, `o` is the number of 1's in `arr`, `dist` is the absolute value of `n/2`, `ans` is either 0 or the value of `pos` when `o_r >= (z_r + o_r) / 2` and `z_l >= (z_l + o_l) / 2` and `(b_d > abs(n / 2 - pos))`, `b_d` is either the absolute value of `n/2` if `o_r >= (z_r + o_r) / 2`, otherwise `b_d` is 30001, `pos` is `n`, `i` is the last element in the list. If `i` is 0, then `z` is increased by 1 and `o` is decreased by 1. Otherwise, `o_l` is increased by 1 and `o_r` is decreased by 1, and the value of `ans` is being printed.
    #
    #The output state after the loop executes all the iterations is that `t` has been decremented to 0, indicating that all test cases have been processed. The remaining variables retain their values from the last iteration of the loop, with `ans` holding the position where the conditions `o_r >= (z_r + o_r) / 2` and `z_l >= (z_l + o_l) / 2` and `(b_d > abs(n / 2 - pos))` were met for the last time, or 0 if these conditions were never met. The input stream is empty, as all test cases have been processed.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer n and a string of length n containing only 0s and 1s. The function calculates the position where the number of 1s to the right of the position is greater than or equal to half of the total number of 1s and 0s to the right, and the number of 0s to the left of the position is greater than or equal to half of the total number of 0s and 1s to the left. If such a position is found, the function prints the position; otherwise, it prints 0. The function continues processing test cases until all input has been consumed.

