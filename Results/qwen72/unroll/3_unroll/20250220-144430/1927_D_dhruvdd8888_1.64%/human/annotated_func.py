#State of the program right berfore the function call: The function `func_1` is expected to read input from stdin and process multiple test cases. Each test case includes an array `a` of integers and a series of queries. The array `a` has a length `n` (2 ≤ n ≤ 2 · 10^5), and each element `a_i` is an integer (1 ≤ a_i ≤ 10^6). The number of queries `q` for each test case is an integer (1 ≤ q ≤ 2 · 10^5). Each query is defined by two integers `l` and `r` (1 ≤ l < r ≤ n). The total sum of `n` and `q` across all test cases does not exceed 2 · 10^5.
def func_1():
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
        
    #State: `arr` is a list of tuples where each tuple represents a range in the `nums` list and the value that was repeated in that range. `s` is the index of the last element in the `nums` list. `e` is 0. `num` is the last element in the `nums` list, which is `-1`.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [nums list with the last element being -1 (the exact content of the list is not provided, but the last element is -1)]
    #State: *`arr` is a list of tuples where each tuple represents a range in the `nums` list and the value that was repeated in that range. `s` is the index of the last element in the `nums` list. `e` is 0. `num` is the last element in the `nums` list, which is `-1`. `LA` is the length of `arr` minus 1. If `ppp` is equal to 23, the postcondition remains unchanged.
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
        
    #State: - After the loop finishes, `s` and `e` will be the values of the last tuple in `arr` that was processed.
    #   - `arr`, `LA`, `num`, and `ppp` will remain unchanged.
    #
    #Given the initial state and the loop code, the output state after all iterations of the loop have finished is:
    #
    #Output State:
#Overall this is what the function does:The function `func_1` reads from standard input and processes multiple test cases. Each test case includes an array `a` of integers and a series of queries. The array `a` has a length `n` (2 ≤ n ≤ 200,000), and each element `a_i` is an integer (1 ≤ a_i ≤ 1,000,000). The number of queries `q` for each test case is an integer (1 ≤ q ≤ 200,000). Each query is defined by two integers `l` and `r` (1 ≤ l < r ≤ n). The function processes the array to identify contiguous ranges of repeated elements and stores these ranges in a list `arr`. For each query, it determines and prints a pair of indices that represent the boundaries of the next or previous range of repeated elements relative to the given range `[l, r]`. If no such range exists, it prints `(-1, -1)`. The function does not return any value; it only prints the results of the queries.

