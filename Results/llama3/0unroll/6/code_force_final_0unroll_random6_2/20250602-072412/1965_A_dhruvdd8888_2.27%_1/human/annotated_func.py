#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is given in the first line of the input.
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None
    #State: The number of test cases is reduced by 1, stdin contains the remaining test cases, N is an integer, nums is a sorted list of distinct integers. The length of nums is more than 1.
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    #State: *The number of test cases is reduced by 1, stdin contains the remaining test cases, N is an integer, nums is a sorted list of distinct integers. The length of nums is more than 2.
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: Output State: The number of test cases remains the same, stdin contains the remaining test cases, N is an integer, nums is a sorted list of distinct integers with 0 added at the beginning, cd is the number of consecutive pairs of integers in nums that differ by 1.
    if (cd & 1) :
        return print('Bob')
        #The program returns and prints the string 'Bob'
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None.

#Overall this is what the function does:Determines the winner of a game based on a set of distinct integers. The function reads input from stdin, processes multiple test cases, and prints the winner's name ('Alice' or 'Bob') for each case. The winner is determined by the length of the input set and the presence of consecutive pairs of integers that differ by 1. If the set contains only one or two elements, the function prints 'Alice' or 'Bob' respectively. Otherwise, it checks for consecutive pairs and prints 'Bob' if the count is odd, or 'Alice' if the count is even. The function returns None in all cases.

