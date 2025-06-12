#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 2 * 10^4) — the number of test cases. For each test case, the first line contains a single integer n (1 <= n <= 2 * 10^5) and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: t is an integer between 1 and 2 * 10^4 inclusive, n is an integer between 1 and 2 * 10^5 inclusive, arr is a list of n integers between 0 and n-1, counter is a dictionary where the keys are the elements in arr and the values are their respective frequencies, _ is t, stdin is empty, ans is either the smallest missing number in arr or the smallest number that appears only once in arr for each test case, once is True if ans is the smallest number that appears only once in arr for the last test case, otherwise once is False. The value of ans for each test case has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. For each test case, it finds and prints the smallest missing number in the list or the smallest number that appears only once in the list, whichever comes first. The function processes all test cases and prints the corresponding results.

