#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 <= a_i < n).
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: tc is equal to the number of test cases, N is an integer greater than or equal to 0, a is a list of N integers, cnt is a dictionary with default value 0 where cnt[a[i]] is increased by 1 for all i in range(N), i is N, t is either 0, 1, or 2, stdin contains no more test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of integers. It then finds the smallest integer that appears only once in the list or is not present in the list, and prints this integer. The function processes all test cases and does not return any value.

