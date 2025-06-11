#State of the program right berfore the function call: stdin contains a sequence of inputs: first an integer t, then for each i in range(t): first an integer n, then a list of n integers, then an integer q, then q pairs of integers.
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
        
    #State: N is at least 0, i is N, nums is a list of n integers followed by -1, s is either 0 or N, e is 0, num is -1, arr is a list of tuples where each tuple contains (1 + s, i, num) for each i where nums[i] != num, stdin contains t-1 sequences of inputs: first an integer n, then a list of n integers, then an integer q, then q pairs of integers.
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
        
    #State: N is at least 0, i is N, nums is a list of n integers followed by -1, s is either 0 or N, e is either 0 or 1 + s, num is -1, arr is a list of tuples where each tuple contains (1 + s, i, num) for each i where nums[i] != num, LA is the second last index of arr, stdin is empty.

#Overall this is what the function does:This function reads a sequence of inputs from standard input, where each sequence consists of an integer t, followed by t sequences of an integer n, a list of n integers, an integer q, and q pairs of integers. It then processes these inputs to find the first and last indices of the first sequence of identical integers that overlap with a given range [l, r] for each query. If no such sequence exists, it prints (-1, -1). The function continues this process until all queries have been processed, at which point the standard input is empty.

