#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n, followed by a list of n integers, followed by an integer q, followed by q pairs of integers. All integers are greater than 0.
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
        
    #State: Output State: The loop iterates N+1 times, and in each iteration, it checks if the current number in the list is different from the previous number. If it is, it appends a tuple to the list 'arr' containing the index of the previous number plus one, the current index, and the previous number. It then updates the variable 's' to the current index. The variable 'num' is updated to the current number in the list in each iteration. After the loop finishes, the variable 's' will be equal to the last index of the list, and the variable 'num' will be equal to the last number in the list. The list 'arr' will contain tuples representing the ranges of consecutive equal numbers in the list.
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
        
    #State: Output State: The variable `_` is assigned the value of the number of iterations of the loop, which is equal to the integer input by the user. The variable `l` is assigned the value of the last left boundary input by the user, and the variable `r` is assigned the value of the last right boundary input by the user. The variable `eli` is assigned the value of the insertion point of the last tuple `(l, 0, 0)` in the list `arr` to maintain sorted order. The variables `s`, `e`, and `_` are assigned the values of the first, second, and third elements of the tuple at the index `min(eli, LA)` in the list `arr`. The variable `LA` remains unchanged.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer N, followed by a list of N integers, and then an integer Q, followed by Q pairs of integers. The function groups consecutive equal numbers in the list into ranges and stores them in a list of tuples. It then answers Q queries, where each query is a pair of integers (l, r). For each query, the function finds the range of consecutive equal numbers that overlaps with the query range [l, r]. If such a range exists, it prints the start and end indices of the overlapping range. If no overlapping range exists, it prints (-1, -1). The function processes all queries for each test case and prints the results.

