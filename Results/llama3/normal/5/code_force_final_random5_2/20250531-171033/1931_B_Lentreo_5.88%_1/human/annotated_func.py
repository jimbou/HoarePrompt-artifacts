#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
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
        
    #State: t is 0, stdin is empty, n is an integer equal to the value of the last test case, nums is an empty list, last is an integer equal to the last element of the last test case, curr is the sum of all non-zero elements in the list minus the last element of the list multiplied by the number of non-zero elements in the list, and i is the last element in the list. If curr is 0, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints 'YES' or 'NO' for each case. It takes no parameters and returns no value. The function's purpose is to determine whether the sum of all non-zero elements in a list minus the last element of the list multiplied by the number of non-zero elements is zero. If the result is zero, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and empties the stdin.

