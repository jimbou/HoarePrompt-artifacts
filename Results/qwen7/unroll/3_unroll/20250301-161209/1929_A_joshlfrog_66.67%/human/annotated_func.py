#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
def func():
    t = int(input())
    for e in range(t):
        l = int(input())
        
        nums = [int(x) for x in input().split()]
        
        x = 0
        
        y = 100000000
        
        for i in range(l):
            if nums[i] > x:
                x = nums[i]
            if nums[i] < y:
                y = nums[i]
        
        print(x - y)
        
    #State: Output State: t is an integer between 1 and 500 (inclusive), and it is now set to the integer input value; l is an integer; nums is a list of integers; x and y are integers with their final values determined by the loop; no other variables are defined or changed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` indicating the number of cases, followed by `n` integers in each case. For each case, it finds the maximum and minimum values within the list of integers and calculates the difference between them. The function then prints this difference for each test case.

