#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then n space-separated integers. n is a positive integer and the integers are positive integers less than or equal to 10^9.
    N = int(input())
    nums = set(input().split())
    nums.add('0')
    nums = sorted(map(int, nums))
    ls = 0
    for i in range(len(nums)):
        nums[i] -= ls
        
        ls += nums[i]
        
    #State: N is a positive integer, nums is a sorted list of N+1 positive integers (including 0) less than or equal to 10^9 that must have at least N+1 elements, ls is equal to the sum of all elements in the original list, i is N, stdin contains t-1 test cases.
    nw = True
    cw = True
    for i in range(len(nums) - 2, 0, -1):
        if nums[i] == 1:
            cw = not nw
        else:
            cw = True
        
        nw = cw
        
    #State: N is a positive integer, nums is a sorted list of N+1 positive integers (including 0) less than or equal to 10^9 that must have at least N+1 elements, ls is equal to the sum of all elements in the original list, i is 1, stdin contains t-1 test cases, nw is equal to cw which is True.
    if cw :
        print('Alice')
        #This is printed: Alice
    else :
        print('Bob')
        #This is printed: Bob
    #State: *N is a positive integer, nums is a sorted list of N+1 positive integers (including 0) less than or equal to 10^9 that must have at least N+1 elements, ls is equal to the sum of all elements in the original list, i is 1, stdin contains t-1 test cases, nw is equal to cw. If nw is True, then 'Alice' is being printed. Otherwise, 'Bob' is being printed.

#Overall this is what the function does:Determines the winner of a game based on a list of integers. The function reads a positive integer N and a list of N space-separated integers from standard input, sorts the list, and then iterates through the list in reverse order to determine the winner. The winner is either 'Alice' or 'Bob', depending on the values in the list. The function prints the winner to the console.

