#State of the program right berfore the function call: stdin contains multiple test cases. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
                break
        
        print(ans)
        
    #State: `t` is 0, `_` is `t`, `n` is undefined, `arr` is undefined, `counter` is undefined, `stdin` contains no input, `ans` is undefined, and `once` is undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then finds the smallest integer between 0 and n (inclusive) that is either missing from the list or appears only once, and prints this integer for each test case.

