#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        h = {}
        
        ans = n
        
        for i in a:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
            if h[i] >= k:
                ams = k - 1
        
        print(ans)
        
    #State: n is an integer equal to the first integer from the input, k is an integer equal to the second integer from the input, a is an empty list, ans is equal to n, h is a dictionary where each key is an integer from the input and the value is the number of times the integer appears in the input, and the value of ans which is equal to n is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, n and k, and the second line contains n integers. The function then counts the occurrences of each integer in the second line and prints the total number of integers, n, if any integer appears at least k times. If no integer appears at least k times, the function still prints the total number of integers, n.

