#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
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
        
    #State: The output state will be the number of test cases (t) followed by t lines, each containing the number of elements in the array (n) that are less than the given value k.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of elements in each test case array that are less than a given value k. It iterates through each test case, counting the occurrences of each element, and updates the count of elements less than k if an element's count reaches k. The function outputs the total count of elements less than k for each test case.

