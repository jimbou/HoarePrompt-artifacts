#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer n, then a list of n integers, then an integer q, and finally q lines each containing two integers. The integers are all positive and n and q are greater than or equal to 2.
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
        
    #State: Output State: N is a positive integer greater than or equal to 2, nums is a list of N positive integers followed by -1, s is N, e is 0, num is -1, arr is a list of tuples where each tuple contains three values: the first value is the index of the first occurrence of a number in nums plus one, the second value is the index of the last occurrence of the same number in nums, and the third value is the number itself, stdin contains multiple test cases minus one test case that has been partially read.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [list of N positive integers, -1] (where N is a positive integer greater than or equal to 2)
    #State: *N is a positive integer greater than or equal to 2, nums is a list of N positive integers followed by -1, s is N, e is 0, num is -1, arr is a list of tuples where each tuple contains three values: the first value is the index of the first occurrence of a number in nums plus one, the second value is the index of the last occurrence of the same number in nums, and the third value is the number itself, LA is the second last index of arr, stdin contains multiple test cases minus one test case that has been partially read. If ppp is 23, the list of N positive integers followed by -1 is being printed.
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
        
    #State: The loop has executed all its iterations, and the output state is as follows: The value of _ is the number of test cases minus one, l and r are the last pair of integers read from the input, eli is the index where the pair (l, 0, 0) should be inserted in arr to maintain sorted order, s, e, and _ are the values of the tuple at index min(eli, LA) in arr, and tc is 5 plus the number of test cases. The values of N, nums, s, e, num, arr, LA, and stdin remain unchanged. If ppp is 23, the list of N positive integers followed by -1 has been printed for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer N, a list of N positive integers, and an integer Q, followed by Q pairs of integers. The function groups consecutive occurrences of the same number in the list and stores the start and end indices of each group. It then reads Q pairs of integers and for each pair, it finds the group that contains the pair and prints the start and end indices of that group if it exists, or -1 -1 otherwise. If a special condition (ppp == 23) is met, it prints the list of N positive integers followed by -1 for each test case. The function continues this process until all test cases have been processed.

