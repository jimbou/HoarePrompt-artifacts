#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, and a list of integers a_1, a_2, ..., a_n where each a_i satisfies 1 <= a_i <= 10^6.
def func():
    num_tests = int(input())
    while num_tests > 0:
        num_tests -= 1
        
        n = int(input())
        
        nums = [int(x) for x in input().split(' ')]
        
        start_year = 0
        
        for x in range(0, len(nums)):
            start_year = ((start_year + 1) // nums[x] + 1) * nums[x]
        
        print(start_year)
        
    #State: `num_tests` is 0, `n` and `nums` are the values from the last test case, `start_year` is the final value calculated for the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates and prints a specific year based on the input integers.

