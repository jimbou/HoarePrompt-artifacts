#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n, followed by a list of n integers, followed by an integer q, followed by q pairs of integers.
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
        
    #State: N is an integer greater than or equal to 0, nums is a list of N+1 integers, s is the last index of nums where nums[i] is not equal to the previous value of num, e is 0, num is the last integer in the list of N integers, arr is a list of tuples containing the start and end indices of each subsequence of equal integers in nums, stdin contains the remaining test cases, i is N.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [list of N+1 integers in nums]
    #State: N is an integer greater than or equal to 0, nums is a list of N+1 integers, s is the last index of nums where nums[i] is not equal to the previous value of num, e is 0, num is the last integer in the list of N integers, arr is a list of tuples containing the start and end indices of each subsequence of equal integers in nums, stdin contains the remaining test cases, i is N, LA is the second last index of arr. If the current value of ppp is 23, the list of N+1 integers which is nums is being printed.
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
        
    #State: N is an integer greater than or equal to 0, nums is a list of N+1 integers, s is the last index of nums where nums[i] is not equal to the previous value of num, e is the end index of the subsequence of equal integers in nums that contains the last index s, num is the last integer in the list of N integers, arr is a list of tuples containing the start and end indices of each subsequence of equal integers in nums, stdin is empty, and i is N.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer N, followed by a list of N integers, and then an integer q, followed by q pairs of integers. The function groups consecutive equal integers in the list into subsequences and stores their start and end indices. For each query pair (l, r), it finds the subsequence that contains the index l and checks if the subsequence's end index is within the range [l, r]. If it is, the function prints the start and end indices of the subsequence. If not, it prints (-1, -1). The function also handles a special case where the current value of ppp is 23, in which case it prints the list of N+1 integers. After processing all queries, the function leaves the standard input empty.

