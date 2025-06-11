#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9). The sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case, indicating whether the input array is non-decreasing or not. The value of 't' remains unchanged, and the input arrays are sorted in ascending order.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It checks if the integers in each test case are in non-decreasing order after sorting and prints 'YES' if they are, and 'NO' otherwise. The function does not modify the input values or store any results, only printing the outcome of each test case to the console.

