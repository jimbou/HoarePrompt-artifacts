#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given in the first line of stdin.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: The output state will be the maximum middle element of every subarray of length 3 in each test case, or the minimum element if the length of the array is 2. The value of `t` will remain unchanged.

#Overall this is what the function does:The function reads a specified number of test cases from standard input, where each test case consists of a list of integers. For each test case, it finds the maximum middle element of every subarray of length 3 and prints this value. If the length of the array is 2, it prints the minimum element instead. The function processes all test cases and outputs the results without modifying the input values.

