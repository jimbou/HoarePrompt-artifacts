#State of the program right berfore the function call: stdin contains t+2*t*n integers, where t is a positive integer, n is a positive integer such that 1 <= n <= 3*10^5, and the sum of n over all test cases does not exceed 3*10^5. The first integer is t, then for each test case, the first integer is n, and the next n integers are a_1, a_2, ..., a_n such that 0 <= a_i <= n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        num_of_lens = {}
        
        nums = list(map(int, input().split()))
        
        for x in nums:
            num_of_lens[x] = num_of_lens.get(x, 0) + 1
        
        res = 0
        
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += math.comb(cnt, 3)
            if cnt >= 2:
                total_sum = sum(i for i in num_of_lens.values() if i != cnt)
                res += math.comb(cnt, 2) * total_sum
        
        print(res)
        
    #State: Output State: `_` is `t`, `n` is a positive integer, `num_of_lens` is a dictionary with all integers in `nums` as keys and their respective counts as values, `nums` is a list of `n` integers, `res` is the sum of the initial value of `res` and the number of ways to choose 2 items from each value in `num_of_lens` without repetition and without order times the sum of all values in `num_of_lens` except the current value, plus the number of ways to choose 3 items from each value in `num_of_lens` without repetition and without order for values that are 3 or more, `cnt` is the last value in `num_of_lens`. `stdin` contains 0 integers, and the value of `res` is being printed.
    #
    #In natural language, the output state after the loop executes all the iterations is that the loop has finished executing, and the final value of `res` is being printed. The loop variable `_` has reached the value of `t`, indicating that the loop has completed all iterations. The variables `n`, `num_of_lens`, `nums`, `res`, and `cnt` retain their values from the last iteration of the loop. The input stream `stdin` is empty, as all input values have been processed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts a series of test cases, where each test case consists of a positive integer n followed by n integers. The function calculates the number of ways to choose 2 or 3 items from the input integers without repetition and without order, and prints the result for each test case. The input stream is emptied after processing all test cases.

