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
        
    #State: N is an integer greater than or equal to 0, i is N, nums is a list of integers between 1 and 10^6 with an additional element -1 at the end, s is N if nums[N] != num, otherwise s is the last index of the list of integers where nums[index] != num, e is 0, num is -1, stdin contains multiple test cases with three inputs remaining: an integer, a list of integers, and a list of pairs of integers. If the first element of nums is equal to num, then arr is an empty list. Otherwise, arr is a list containing tuples (1 + s, i, num) for each i where nums[i] != num.
    LA = len(arr) - 1
    if (ppp == 23) :
        print(nums)
        #This is printed: a list of integers between 1 and 10^6 with an additional element -1 at the end
    #State: *N is an integer greater than or equal to 0, i is N, nums is a list of integers between 1 and 10^6 with an additional element -1 at the end, s is N if nums[N] != num, otherwise s is the last index of the list of integers where nums[index] != num, e is 0, num is -1, LA is -1 if the first element of nums is equal to num, otherwise LA is the number of elements in arr minus 1, stdin contains multiple test cases with three inputs remaining: an integer, a list of integers, and a list of pairs of integers. If the first element of nums is equal to num, then arr is an empty list. Otherwise, arr is a list containing tuples (1 + s, i, num) for each i where nums[i] != num. If ppp is 23, the list of integers nums is printed.
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
        
    #State: N is an integer greater than or equal to 0, i is N, nums is a list of integers between 1 and 10^6 with an additional element -1 at the end, s is the value of the second element of the tuple at index min(eli, LA) in arr, e is the value of the third element of the tuple at index min(eli, LA) in arr, num is -1, LA is -1 if the first element of nums is equal to num, otherwise LA is the number of elements in arr minus 1, stdin is empty, and the values of l and r are not defined. If s is greater than the first integer from the input, then if s is equal to 1, -1, -1 is printed. Otherwise, s - 1, s is printed. If s is not greater than the first integer from the input, then if e is greater than or equal to the second integer from the input, -1, -1 is printed. If e is less than N, s, e plus 1 are printed. Otherwise, -1, -1 is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It first reads an integer N and a list of integers, and then creates a list of tuples based on the input. The function then reads additional input pairs of integers and uses the created list to determine the output for each pair. If the first element of the pair is greater than a certain value, it prints -1, -1 or s-1, s. If the first element is not greater, it prints -1, -1 or s, e+1, depending on the value of e. The function continues this process until all input pairs have been processed. If a specific condition (ppp == 23) is met, it prints the list of integers.

