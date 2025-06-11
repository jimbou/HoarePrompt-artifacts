#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: stdin contains t-1 test cases, n is an integer between 1 and 100, a is an empty list, ans is 0, cnt is a dictionary with keys as integers from the list and their values as the frequency of each integer, x is the last integer in the list
    for x in cnt.values():
        ans += x // 3
        
    #State: `stdin` contains t-1 test cases, `n` is an integer between 1 and 100, `a` is an empty list, `ans` is increased by the sum of all values in `cnt` divided by 3, `cnt` is a dictionary with all key-value pairs, `x` is the last value in `cnt`.
    print(ans)
    #This is printed: ans (where ans is the sum of all values in cnt divided by 3)

#Overall this is what the function does:This function reads a sequence of integers from standard input, counts the frequency of each integer, and prints the sum of the integer frequencies divided by 3. It processes multiple test cases, where each test case consists of an integer n followed by n integers. The function does not modify the input values or store them after processing.

