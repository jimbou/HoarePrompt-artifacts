#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer n, then a list of n integers, then an integer q, and finally q lines each containing two integers l and r.
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
        
    #State: N is an integer, nums is a list of N+1 integers, s is N, e is 0, num is the last integer in nums, stdin contains multiple test cases minus one test case, and arr is a list containing tuples (1 + s, i, num) for each i where nums[i] is not equal to the previous value of num.
    LA = len(arr) - 1
    for _ in range(int(input())):
        l, r = tuple(map(int, input().split()))
        
        eli = bisect_left(arr, (l, 0, 0))
        
        s, e, _ = arr[min(eli, LA)]
        
        if s > l:
            if s == 1 or s > r:
                print(-1, -1)
            else:
                print(s - 1, s)
        elif e >= r:
            print(-1, -1)
        elif e < N or e < l:
            print(s, e + 1)
        else:
            print(-1, -1)
        
    #State: N is an integer, nums is a list of N+1 integers, s is the second element of the tuple at index min(eli, LA) in arr, e is the third element of the tuple at index min(eli, LA) in arr, num is the last integer in nums, stdin is empty, arr is a list containing tuples (1 + s, i, num) for each i where nums[i] is not equal to the previous value of num, LA is the second last index of arr, l is an integer, r is an integer, eli is the insertion point for (l, 0, 0) in arr to maintain sorted order.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains an integer N, a list of N integers, an integer Q, and Q lines of queries. For each query, it finds the first and last indices of the first sequence of identical integers that overlaps with the query range [l, r]. If no such sequence exists, it returns (-1, -1). If the sequence starts after the query range, it returns the indices of the sequence that immediately precedes the query range. If the sequence ends before the query range, it returns the indices of the sequence that immediately follows the query range. The function prints the result for each query.

