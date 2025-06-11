#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a positive integer n. The second line contains n positive integers. The sum of n over all test cases does not exceed 2 * 10^5.
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: `n` is 0, `a` is an empty list, `cnt` is a list of integers where all elements are 0, `x` is the last element in the list `cnt`, `ans` is 0, stdin is empty, and nothing is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer n followed by n positive integers. It then calculates and prints the sum of the counts of each integer minus one, effectively counting the number of pairs of identical integers in each test case. After processing all test cases, the function leaves the input stream empty and does not print anything further.

