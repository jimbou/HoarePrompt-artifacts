#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 2 * 10^5), then n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9) such that the sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: t is 0, n is an integer, arr is a sorted list of integers, stdin is empty. If all elements in arr are in non-decreasing order, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether the input integers in each test case are in non-decreasing order. It prints 'YES' if the integers are in non-decreasing order and 'NO' otherwise. The function consumes all input from stdin and does not return any value.

