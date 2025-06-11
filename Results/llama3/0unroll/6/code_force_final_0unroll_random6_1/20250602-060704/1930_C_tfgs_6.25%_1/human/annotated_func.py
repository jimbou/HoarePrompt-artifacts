#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 3 * 10^5). The second line contains n integers a_1,a_2,...,a_{n} (1 ≤ a_i ≤ 10^9). The sum of n over all test cases does not exceed 3 * 10^5.
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: n is an integer equal to the number of integers in the last test case, a is a list of integers equal to the last test case where each integer at index i is incremented by i + 1, stdin is empty.
    counter = Counter(a)
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, counter[a[i - 1]])
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            counter[a[i - 1]] -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
    #State: Output State: The loop has executed all iterations, and the output state is as follows: n remains the same, a is unchanged, counter has been updated with decremented values for each integer, cnt is 0, ans is a list containing all integers from the last test case in descending order, with duplicates inserted in the correct positions, and stdin is still empty.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: The loop has executed all iterations, and the output state is as follows: n remains the same, a is unchanged, counter has been updated with decremented values for each integer, cnt is 0, ans is a list containing all integers from the last test case in descending order, with duplicates inserted in the correct positions, and stdin is still empty.
    print(*ans)
    #This is printed: the list of integers from the last test case in descending order, with duplicates inserted in the correct positions

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. For each test case, it increments each integer by its 1-based index, removes duplicates, sorts the integers in descending order, and inserts duplicates in the correct positions to maintain the original count of each integer. Finally, it prints the resulting list of integers for each test case.

