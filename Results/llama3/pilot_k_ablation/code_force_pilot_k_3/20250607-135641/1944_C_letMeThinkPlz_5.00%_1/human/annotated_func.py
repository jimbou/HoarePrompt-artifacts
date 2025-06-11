#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n).
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
        
    #State: t is 0, _ is t, n is greater than or equal to 0, counter is a dictionary where the count of each integer in arr is incremented by the number of times it appears in arr, arr is a list of n integers from the last input, stdin contains no lines, ans is either 0, 1, or the value of i + 1 when the count of i in counter is 1 and once is False, and once is True if the count of i in counter is 1 and once is False, otherwise once is False, and ans is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by a line of n integers. It then finds the smallest missing non-negative integer in the range [0, n) that appears either zero or one times in the input list. If no such integer is found, it prints 0. Otherwise, it prints the smallest missing integer that appears zero times or the smallest integer that appears once, whichever is smaller. The function processes all test cases and prints the corresponding results.

