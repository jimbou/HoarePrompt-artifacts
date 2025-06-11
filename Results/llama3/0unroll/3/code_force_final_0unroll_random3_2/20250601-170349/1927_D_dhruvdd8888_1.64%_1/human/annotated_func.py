#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer n, then a list of n integers, then an integer q, and then q pairs of integers. n and q are non-negative integers and n is greater than 1.
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    s = 0
    e = 0
    num = nums[0]
    arr = []
    nums.append(-1)
    for i in range(N + 1):
        if nums[i] != num:
            arr.append((1 + s, i, num))
            s = i
        
        num = nums[i]
        
    #State: Output State: N is a non-negative integer, nums is a list of N+1 integers, s is N, e is 0, num is the last integer in the list of N integers, arr is a list of tuples, each containing three integers, stdin contains multiple test cases with three inputs remaining: an integer q, and then q pairs of integers.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: A list of N+1 integers (where N is a non-negative integer)
    #State: *N is a non-negative integer, nums is a list of N+1 integers, s is N, e is 0, num is the last integer in the list of N integers, arr is a list of tuples, each containing three integers, LA is the second last index of arr, stdin contains multiple test cases with three inputs remaining: an integer q, and then q pairs of integers. If the current value of ppp is 23, the list of N+1 integers, nums, is printed.
    for _ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        
        if tc > 5:
            if ppp == 23:
                print(l, r)
            continue
        
        eli = bisect_left(arr, (l, 0, 0))
        
        s, e, _ = arr[min(eli, LA)]
        
        if s > l:
            if s == 1:
                print(-1, -1)
            else:
                print(s - 1, s)
        elif e >= r:
            print(-1, -1)
        elif e < N:
            print(s, e + 1)
        else:
            print(-1, -1)
        
    #State: The loop iterates over the input test cases, and for each test case, it calculates the values of s, e, and _ based on the input values l and r. If the current value of ppp is 23, it prints the list of N+1 integers, nums. The loop continues until all test cases have been processed. The final state of the variables is: N remains unchanged, nums remains unchanged, s and e have been updated based on the last test case, num remains unchanged, arr remains unchanged, LA remains unchanged, and stdin is empty.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer N, a list of N integers, an integer q, and q pairs of integers. The function groups consecutive equal integers in the list and stores the start and end indices of each group. Then, for each query pair (l, r), it finds the group that contains l and checks if r is within the same group. If so, it prints the start and end indices of the group. If not, it prints -1 -1. If the current value of ppp is 23, it prints the list of N+1 integers. The function continues processing test cases until all input has been consumed.

