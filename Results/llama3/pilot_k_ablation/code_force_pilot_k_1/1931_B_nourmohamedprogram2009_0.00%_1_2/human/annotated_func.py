#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_i <= 10^9). The sum of a_i is divisible by n.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: t is 0, stdin is empty, _ is t, n is not defined, arr is not defined.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers, and checks if the integers are sorted in non-decreasing order. For each test case, it prints 'YES' if the integers are sorted and 'NO' otherwise.

