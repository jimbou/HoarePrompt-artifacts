#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        
        ans = 0
        
        once = False
        
        for i in range(n):
            if counter.get(i, 0) == 0:
                ans = i
                break
            elif counter.get(i, 0) == 1 and not once:
                once = True
                ans = i + 1
            elif counter.get(i, 0) == 1:
                ans = i
                break
        
        print(ans)
        
    #State: `t` is 0, `stdin` is empty, `n` is undefined, `arr` is undefined, `counter` is undefined, `ans` is undefined, `once` is undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. It then finds the smallest positive integer that is not present in the list or the smallest positive integer that appears only once in the list, and prints this value for each test case. The function processes all test cases and leaves the input stream empty.

