#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then n integers a_1, a_2, \ldots, a_n. 1 <= t <= 100, 1 <= n <= 100, and 1 <= a_i <= 100.
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: stdin contains t-1 test cases, n is an integer, a is an empty list, x is the last integer in the original list, ans is 0, cnt is a dictionary with all integers from the original list as keys and their values are the number of times each integer appeared in the original list.
    for x in cnt.values():
        ans += x // 3
        
    #State: stdin contains t-1 test cases, n is an integer, a is an empty list, x is the last value in the cnt dictionary, ans is equal to the initial value of ans (which is 0) plus the sum of the integer division of all values in cnt by 3, cnt is a dictionary with all integers from the original list as keys and their values are the number of times each integer appeared in the original list.
    print(ans)
    #This is printed: the total number of groups of 3 that can be formed from the integers in the original list

#Overall this is what the function does:This function reads a list of integers from standard input, counts the occurrences of each integer, and calculates the total number of groups of 3 that can be formed from these integers. It then prints this total count. The function processes one test case at a time, with the number of test cases specified at the beginning of the input.

