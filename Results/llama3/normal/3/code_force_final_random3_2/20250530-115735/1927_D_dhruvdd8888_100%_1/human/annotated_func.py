#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of integers, then an integer, and then a list of pairs of integers. The first integer is the length of the list of integers. The second integer is the number of pairs of integers. The list of integers contains integers between 1 and 10^6. The list of pairs of integers contains pairs of integers between 1 and the length of the list of integers.
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
        
    #State: N is at least 0, i is N, nums is a list of integers between 1 and 10^6 with an additional -1 at the end, num is -1, s is the index of the last integer in the list of integers that is not equal to the first integer in the original list of integers, e is 0, and arr is a list containing tuples (1 + s, i, num) for each integer in the list of integers that is not equal to the first integer in the original list of integers.
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
        
    #State: N is at least 0, i is N, nums is a list of integers between 1 and 10^6 with an additional -1 at the end, num is -1, s is the index of the last integer in the list of integers that is not equal to the first integer in the original list of integers, e is the value of the second element of the tuple at index min(eli, LA) in arr, l and r are integers greater than 0, eli is the insertion point for (l, 0, 0) in arr to maintain sorted order, LA is the last index of arr, and stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers and a number of pairs of integers. It then processes each pair of integers by finding the first and last indices of the range that contains the pair, and prints the indices if the range is valid, otherwise prints -1 -1. The function repeats this process for all pairs in all test cases until standard input is empty.

