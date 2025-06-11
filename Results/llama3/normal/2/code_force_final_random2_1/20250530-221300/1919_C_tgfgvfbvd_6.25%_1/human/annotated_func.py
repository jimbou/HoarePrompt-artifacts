#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: `n` is an integer, `l` is a list of integers, `y` is an integer less than or equal to `n`, `_` is an integer greater than or equal to 0, `x` is `n`, `a` and `b` are either the current or previous values of `l[x]` or the first element of `l`, and `c` is an integer between 0 and `n - y - 1`

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes the list to find the number of elements that are either greater than or less than the previous elements, and updates two variables (a and b) accordingly. The function prints the count of such elements (c) for each test case.

