#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then a space-separated list of n integers (1 <= a_i <= 10^9).
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: nums is a sorted list of n+1 integers with nums[i] equal to its original value plus the sum of all previous elements minus ls, ls is equal to (i+1) times its original value plus the sum of all previous elements minus the sum of all elements at indices greater than i, i is equal to n, N is an integer between 1 and 2*10^5 inclusive, stdin contains t-n test cases.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: `nums` is a sorted list of n+1 integers with nums[i] equal to its original value plus the sum of all previous elements minus ls, ls is equal to (i+1) times its original value plus the sum of all previous elements minus the sum of all elements at indices greater than i, i is equal to 1, N is an integer between 1 and 2*10^5 inclusive, stdin contains t-n test cases, nw is the opposite of its previous value, and cw is the opposite of its previous value, and nums has at least 3 elements. If the current value of nums[i] is 1, then cw is False and nw is False. Otherwise, cw is True and nw is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: nums is a sorted list of n+1 integers with nums[i] equal to its original value plus the sum of all previous elements minus ls, ls is equal to (i+1) times its original value plus the sum of all previous elements minus the sum of all elements at indices greater than i, i is equal to 1, N is an integer between 1 and 2*10^5 inclusive, stdin contains t-n test cases, nw is the opposite of its previous value, and cw is the opposite of its previous value, and nums has at least 3 elements. If the current value of nums[i] is 1, then nw is False and cw is False. Otherwise, nw is True and cw is True. Additionally, if cw is True, then 'Alice' is printed and nw is True if nums[i] is not 1. If cw is False, then 'Bob' is printed.

#Overall this is what the function does:This function determines the winner of a game based on a list of integers. It takes no parameters and returns no value, but instead prints the name of the winner ('Alice' or 'Bob'). The function reads input from stdin, processes it, and then prints the result. The input is expected to contain a series of test cases, each consisting of an integer n followed by a list of n integers. The function modifies the input list by adding a '0' element, sorting it, and then transforming the values based on their position in the list. It then iterates over the list in reverse order, updating two boolean variables (nw and cw) based on the values in the list. Finally, it prints the name of the winner based on the value of the cw variable.

