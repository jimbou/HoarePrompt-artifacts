#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9). The sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().strip().split()))
        
        last = nums[-1]
        
        curr = 0
        
        for i in nums:
            if i != 0:
                curr += i - last
        
        if curr == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The output state is a list of 'YES' or 'NO' for each test case, indicating whether the sum of the differences between each non-zero number and the last number in the list is zero or not. The value of `t` remains unchanged, and the input is consumed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs a list of 'YES' or 'NO' values. For each test case, it takes a list of integers, calculates the sum of differences between each non-zero number and the last number in the list, and prints 'YES' if the sum is zero, otherwise prints 'NO'. The function consumes the input and leaves the value of `t` unchanged.

