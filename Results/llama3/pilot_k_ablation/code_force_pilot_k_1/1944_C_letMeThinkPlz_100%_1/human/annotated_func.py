#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
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
        
    #State: `t` is an integer (1 ≤ t ≤ 2 * 10^5), stdin contains no input, `_` is `t-1`, `n` is an integer, `arr` is a list of integers, `counter` is a dictionary where each key is an integer from `arr` and its corresponding value is the count of that integer in `arr`, `ans` is the smallest integer that appears at most once in `arr` if such an integer exists, otherwise `ans` is the smallest integer that does not appear in `arr`, and `once` is True if and only if there is an integer that appears exactly once in `arr`, and the smallest integer that appears at most once in `arr` if such an integer exists, otherwise the smallest integer that does not appear in `arr` has been printed `t` times.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds and prints the smallest integer that appears at most once in the list. If no such integer exists, it prints the smallest integer that does not appear in the list. This process is repeated for each test case.

