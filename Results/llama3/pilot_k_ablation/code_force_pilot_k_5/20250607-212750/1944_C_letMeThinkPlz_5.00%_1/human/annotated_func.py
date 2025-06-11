#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. The description of the test cases follows. The first line of each test case contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: t is 0, _ is t, n is an integer that must be greater than or equal to t, arr is a list of integers that must have at least t elements, counter is a dictionary where each key is an element in the list and the value is the number of occurrences of that element, stdin is empty, ans is the smallest number that is not in the list or the smallest number that appears only once in the list and is greater than the last element in the list, once is True, i is the last element in the list, and ans is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds and prints the smallest number that is either not present in the list or appears only once in the list and is greater than the last element in the list. The function processes all test cases and prints the corresponding results.

