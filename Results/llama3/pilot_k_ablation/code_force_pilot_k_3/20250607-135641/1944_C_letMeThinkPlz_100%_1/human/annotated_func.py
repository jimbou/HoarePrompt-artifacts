#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 <= a_i < n).
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
        
    #State: t is 0, stdin is empty, n is an integer between 1 and 2 * 10^5 (inclusive), arr is a list of n integers, counter is a dictionary where each key is an integer from arr and its value is the number of times it appears in arr, i is n, ans is the smallest integer that is not present in arr or is present only once in arr, and once is True if there is an integer that is present only once in arr and False otherwise.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. It then finds and prints the smallest integer that is either missing from the list or appears only once in the list. The function processes all test cases and leaves the standard input empty after execution.

