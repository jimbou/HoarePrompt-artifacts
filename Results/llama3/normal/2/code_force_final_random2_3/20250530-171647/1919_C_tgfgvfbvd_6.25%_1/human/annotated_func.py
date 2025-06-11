#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
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
        
    #State: n is an integer, l is a list of integers, a is the minimum value in the list l, b is the maximum value in the list l, c is the number of times a value in the list l is greater than both a and b, y is n - 1, stdin is empty, _ is the number of test cases, and x is no longer defined, and the number of times a value in the list l is greater than both a and b which is c is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds the minimum and maximum values in the list and counts the number of times a value in the list is greater than both the minimum and maximum values. The function prints this count for each test case.

