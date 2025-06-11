#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 100) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 100) followed by n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: stdin is empty, n is an integer between 1 and 100, a is a list of n integers between 1 and 100, ans is 0, cnt is a dictionary where the keys are the unique integers in list a and the values are their respective counts.
    for x in cnt.values():
        ans += x // 3
        
    #State: Output State: stdin is empty, n is an integer between 1 and 100, a is a list of n integers between 1 and 100, ans is the sum of the integer division of each count in cnt by 3, cnt is a dictionary where the keys are the unique integers in list a and the values are their respective counts.
    print(ans)
    #This is printed: sum of the integer division of each count in cnt by 3 (where cnt is a dictionary of unique integers in list a and their respective counts)

#Overall this is what the function does:This function reads a list of integers from standard input, counts the occurrences of each unique integer, and then calculates the sum of the integer divisions of these counts by 3. The result is then printed to the console.

