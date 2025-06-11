#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 100) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `stdin` contains `t-1` test cases, `n` is an integer between 1 and 100, `a` is an empty list, `x` is the last integer in the original list `a`, `ans` is 0, `cnt` is a dictionary with all integers from the original list `a` as keys and their values are the counts of each integer in the original list `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: `stdin` contains `t-1` test cases, `n` is an integer between 1 and 100, `a` is an empty list, `x` is the last value in the dictionary `cnt`, `ans` is increased by the integer division of all values in the dictionary `cnt` by 4, `cnt` is a dictionary with all integers from the original list `a` as keys and their values are the counts of each integer in the original list `a`.
    print(ans)
    #This is printed: ans (where ans is the sum of the integer divisions of all values in the dictionary cnt by 4)

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of an integer n followed by n integers. It counts the occurrences of each integer, then calculates the sum of the integer divisions of these counts by 4. Finally, it prints this sum to standard output.

