#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a = l[0]
        
        b = 0
        
        c = 0
        
        y = 0
        
        for y in range(1, n):
            if l[y] > l[y - 1]:
                b = l[y]
                break
        
        for x in range(y + 1, n):
            if l[x] > a and l[x] > b:
                if l[x] - a >= l[x] - b:
                    a = l[x]
                else:
                    b = l[x]
                c += 1
            elif l[x] < a and l[x] < b:
                if a - l[x] <= b - l[x]:
                    a = l[x]
                else:
                    b = l[x]
            elif a >= l[x]:
                a = l[x]
            else:
                b = l[x]
        
        print(c)
        
    #State: The number of times a subsequence of three numbers (a, b, c) is found in the input list such that a < b < c and the difference between a and c is greater than or equal to the difference between b and c.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then analyzes each list to find the number of times a subsequence of three numbers (a, b, c) appears, where a < b < c and the difference between a and c is greater than or equal to the difference between b and c. The function prints the count of such subsequences for each test case.

