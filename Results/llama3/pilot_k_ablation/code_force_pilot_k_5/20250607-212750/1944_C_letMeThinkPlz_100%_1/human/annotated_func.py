#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: t is 0, _ is t, stdin contains multiple test cases - t test cases less than before, n is an integer between 1 and 2 * 10^5, arr is an empty list, counter is a dictionary with all elements of arr as keys and their respective counts, ans is the smallest integer between 0 and n-1 that is not present in the counter dictionary or has a count of 1, once is True, and i is n, and the smallest integer between 0 and n-1 that is not present in the counter dictionary or has a count of 1 which is ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then finds the smallest integer between 0 and n-1 that is either missing from the list or appears only once, and prints this integer for each test case.

