#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: cnt is a dictionary where the key is the integer from the list a and the value is the frequency of that integer in the list a.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: 

#Overall this is what the function does:This function takes no arguments and returns the smallest integer that appears either zero or more than one times in the input list of integers. The function reads input from stdin, processes multiple test cases, and returns the result for each test case. The input list contains n integers, and the function iterates through the list to count the frequency of each integer. It then iterates through the range of possible integers (from 0 to n) and returns the smallest integer that meets the condition of appearing either zero or more than one times in the list. If no such integer is found, the function returns the value of n.

