#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer n, then a list of n integers, then an integer q, and finally q pairs of integers. The integers in the list are between 1 and 10^6. The integers in the pairs are between 1 and n.
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
        
    #State: Output State: The loop has executed N+1 iterations. The variable 'i' has the value N, 'num' has the value -1, 's' has the value N, and 'arr' contains N tuples, each representing a subarray of the original list of N integers. The first element of each tuple is the starting index of the subarray plus one, the second element is the ending index of the subarray, and the third element is the value of the subarray. The 'nums' list and the 'e' variable remain unchanged.
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
        
    #State: Output State: The loop has executed 0 iterations. The variable 'i' has the value 0, 'num' has the value -1, 's' has the value 0, 'arr' contains 0 tuples, each representing a subarray of the original list of 0 integers. The first element of each tuple is the starting index of the subarray plus one, the second element is the ending index of the subarray, and the third element is the value of the subarray. The 'nums' list and the 'e' variable remain unchanged. 'LA' has the value -1.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer n, a list of n integers, an integer q, and q pairs of integers. It groups consecutive equal integers in the list into subarrays and stores their start and end indices, along with the integer value. Then, for each query pair (l, r), it finds the subarray that contains the range [l, r] and prints the start and end indices of the subarray if it exists, or (-1, -1) if no such subarray is found. The function handles edge cases where the range [l, r] is not fully contained within a subarray or is outside the bounds of the list.

