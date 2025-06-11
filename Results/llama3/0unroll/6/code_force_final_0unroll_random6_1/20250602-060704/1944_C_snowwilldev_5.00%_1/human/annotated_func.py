#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 * 10^4). Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: The output will be the smallest number that appears either zero or two or more times in the list. If no such number exists, it will be the smallest number that appears exactly once.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains a list of integers. It identifies and prints the smallest number in the list that appears either zero, two, or more times. If no such number exists, it prints the smallest number that appears exactly once.

