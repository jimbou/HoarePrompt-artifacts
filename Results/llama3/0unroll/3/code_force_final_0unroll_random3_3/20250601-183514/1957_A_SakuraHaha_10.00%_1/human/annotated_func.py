#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: stdin contains t-1 test cases, n is an integer between 1 and 100 inclusive, a is a list of n integers between 1 and 100 inclusive, ans is 0, cnt is a dictionary where keys are the unique integers in list a and values are their respective counts.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: ans is the sum of the integer division of the count of each unique integer in list a by 4, cnt remains unchanged as a dictionary where keys are the unique integers in list a and values are their respective counts, n remains unchanged as an integer between 1 and 100 inclusive, a remains unchanged as a list of n integers between 1 and 100 inclusive, stdin contains t-1 test cases.
    print(ans)
    #This is printed: sum of integer divisions of counts of unique integers in list a by 4 (where counts are stored in dictionary cnt)

#Overall this is what the function does:This function reads a list of integers from standard input, counts the occurrences of each unique integer, calculates the sum of the integer divisions of these counts by 4, and prints the result.

