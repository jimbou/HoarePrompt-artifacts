#State of the program right berfore the function call: stdin contains a series of test cases. Each test case consists of a line with an integer n, a line with n space-separated integers, a line with an integer q, and q lines with two space-separated integers each.
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
        
    #State: Output State: N is an integer, nums is a list of N+1 integers, s is N, e is 0, num is the last integer in the original list of N integers, arr is a list of tuples containing the indices of the first occurrence of each integer in the original list of N integers along with the integer itself, stdin contains the remaining test cases.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: [list of N+1 integers]
    #State: N is an integer, nums is a list of N+1 integers, s is N, e is 0, num is the last integer in the original list of N integers, arr is a list of tuples containing the indices of the first occurrence of each integer in the original list of N integers along with the integer itself, LA is the second last index of arr, stdin contains the remaining test cases, and if ppp is equal to 23, the list of N+1 integers which is nums is being printed.
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
        
    #State: Output State: The loop has executed all its iterations, and the output state is as follows: The value of the variable "tc" has been incremented by the number of test cases in the input. The list "nums" remains unchanged. The variable "ppp" remains unchanged. The list "arr" remains unchanged. The variable "LA" remains unchanged. The variable "stdin" is empty, as all the test cases have been processed. The variables "s", "e", and "num" have been updated according to the last test case processed.

#Overall this is what the function does:This function processes a series of test cases from standard input. Each test case consists of a list of integers and a set of queries. The function groups consecutive occurrences of the same integer in the list and stores the start and end indices of each group. For each query, it finds the group that contains the query range and returns the start and end indices of that group. If no such group exists, it returns -1, -1. The function also prints the list of integers and the query ranges for debugging purposes if a certain condition is met.

