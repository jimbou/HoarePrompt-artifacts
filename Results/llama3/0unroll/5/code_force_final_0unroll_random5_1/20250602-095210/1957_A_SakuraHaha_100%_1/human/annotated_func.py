#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 100) followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: n is an integer between 1 and 100, a is a list of n integers between 1 and 100, ans is 0, cnt is a dictionary where keys are unique elements from list a and values are their respective counts, stdin is empty.
    for x in cnt.values():
        ans += x // 3
        
    #State: Output State: ans is the sum of the integer divisions of the counts of unique elements in list a by 3, cnt is a dictionary where keys are unique elements from list a and values are their respective counts, n is an integer between 1 and 100, a is a list of n integers between 1 and 100, stdin is empty.
    print(ans)
    #This is printed: the sum of the integer divisions of the counts of unique elements in list a by 3

#Overall this is what the function does:This function reads an integer n and a list of n integers from standard input, counts the occurrences of each unique integer, calculates the sum of the integer divisions of these counts by 3, and prints the result.

