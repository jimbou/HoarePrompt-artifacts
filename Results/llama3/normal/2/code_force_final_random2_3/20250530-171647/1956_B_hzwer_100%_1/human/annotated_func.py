#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `n` is an integer, `a` is a list of integers, `cnt` is a list of `n+1` integers where `cnt[x]` is the number of occurrences of `x` in `a` and the rest are the number of occurrences of their respective indices in `a` and `cnt` is not empty, `x` is the last element in the list `cnt`, `ans` is the sum of max(0, y - 1) for all y in cnt, `stdin` contains no input, _ is n+1, and the sum of max(0, y - 1) for all y in cnt which is equal to ans is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It counts the occurrences of each integer in the list and calculates the sum of the maximum of 0 and the count minus 1 for each integer. The function then prints this sum for each test case.

