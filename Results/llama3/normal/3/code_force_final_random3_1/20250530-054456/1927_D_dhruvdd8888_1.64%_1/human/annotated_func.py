#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer n, then a list of n integers, then an integer q, and then q pairs of integers. The integer n is greater or equal than 2. The integers in the list are between 1 and 10^6. The integer q is greater or equal than 1. The pairs of integers are such that the first integer is less than the second integer and both are between 1 and n.
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
        
    #State: N is an integer greater or equal to 2, nums is a list of N+1 integers, the first N integers are between 1 and 10^6, the last integer is -1, num is -1, s is N, e is 0, arr is a list of tuples, where each tuple contains (1 + previous value of s, previous value of i, previous value of num), i is N, and stdin contains one test case with three inputs: an integer q, and then q pairs of integers.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [list of N integers between 1 and 10^6, -1]
    #State: *N is an integer greater or equal to 2, nums is a list of N+1 integers, the first N integers are between 1 and 10^6, the last integer is -1, num is -1, s is N, e is 0, arr is a list of tuples, where each tuple contains (1 + previous value of s, previous value of i, previous value of num), i is N, LA is the length of arr minus 1, and stdin contains one test case with three inputs: an integer q, and then q pairs of integers. If ppp equals 23, the list of N+1 integers, nums, is printed, where the first N integers are between 1 and 10^6, and the last integer is -1.
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
        
    #State: N is an integer greater or equal to 2, nums is a list of N+1 integers, the first N integers are between 1 and 10^6, the last integer is -1, num is -1, s is the value of the first element of the tuple at index min(eli, LA) in arr, e is the value of the second element of the tuple at index min(eli, LA) in arr, arr is a list of tuples, where each tuple contains (1 + previous value of s, previous value of i, previous value of num), i is N, LA is the length of arr minus 1, eli is the insertion point of (l, 0, 0) in arr to maintain sorted order, l is the first integer of the last test case, r is the second integer of the last test case, and stdin is empty. If s > l, then if s is 1, -1, -1 is printed. Otherwise, s - 1 and s are printed. If s is not greater than l, then if e is greater or equal to r, -1, -1 is printed. Otherwise, if e is less than N, the values of s and e+1 are printed. Otherwise, -1, -1 is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer N, a list of N integers, an integer q, and q pairs of integers. The function first processes the list of integers to create a list of tuples, where each tuple contains the start and end indices of a subsequence of equal integers. Then, for each pair of integers (l, r), the function finds the corresponding subsequence and prints the start and end indices if the subsequence is within the range [l, r], or -1, -1 if not. If the current value of ppp is 23, the function also prints the list of N+1 integers.

