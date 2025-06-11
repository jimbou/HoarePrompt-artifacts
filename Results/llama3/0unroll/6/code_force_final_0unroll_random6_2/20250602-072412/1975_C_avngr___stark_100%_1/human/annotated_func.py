#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: The output state after the loop executes all the iterations is the maximum middle element of each subarray of length 3 in the input list `a`, or the minimum element if the length of the list is 2. The output is printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. For each test case, it finds the maximum middle element of each subarray of length 3 in the input list, or the minimum element if the list has only 2 elements, and prints the result.

