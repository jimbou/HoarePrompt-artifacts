#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2*10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    N = int(input())
    nums = set(input().split())
    nums = sorted(map(int, nums))
    if (len(nums) == 1) :
        return print('Alice')
        #The program prints 'Alice' and returns None.
    #State: *N is an integer between 1 and 10^4, nums is a sorted list of unique integers between 1 and 10^9, stdin is empty. The length of nums is more than 1
    if (len(nums) == 2) :
        return print('Bob')
        #The program prints 'Bob' and returns None.
    #State: *N is an integer between 1 and 10^4, nums is a sorted list of unique integers between 1 and 10^9, stdin is empty. The length of nums is more than 2
    nums.insert(0, 0)
    cd = 0
    for i in range(len(nums) - 2):
        if nums[i + 1] - nums[i] == 1:
            cd += 1
        else:
            break
        
    #State: N is an integer between 1 and 10^4, nums is a sorted list of unique integers between 1 and 10^9 with a prepended 0, stdin is empty, i is len(nums) - 2, and cd is the number of consecutive pairs of elements in nums that have a difference of 1, starting from the first element.
    if (cd & 1) :
        return print('Bob')
        #The program prints 'Bob' and returns None
    else :
        return print('Alice')
        #The program prints 'Alice' and returns None

#Overall this is what the function does:This function determines the winner of a game based on a set of unique integers. It reads an integer N from standard input, followed by N integers, and then analyzes the sequence of numbers. If the sequence has only one or two unique numbers, it prints 'Alice' or 'Bob', respectively. Otherwise, it checks for consecutive pairs of numbers with a difference of 1 and prints 'Bob' if the count of such pairs is odd, or 'Alice' if the count is even. The function returns None in all cases.

