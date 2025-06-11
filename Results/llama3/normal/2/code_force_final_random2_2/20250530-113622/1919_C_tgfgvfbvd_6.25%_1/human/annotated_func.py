#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 ≤ n ≤ 2*10^5) and then a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n).
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
        
    #State: n is an integer greater than or equal to 1, l is a list of n integers between 1 and n, x is equal to n, y is n - 1, c is either 0, 1, 2, ..., or n - 1. a is either the maximum integer in the list l or the first integer in the list l that is greater than the previous integer and is less than the maximum integer in the list l. b is either the maximum integer in the list l or the first integer in the list l that is greater than the previous integer and is less than the maximum integer in the list l, and the value of c which is either 0, 1, 2, ..., or n - 1 is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes the list to find the maximum number of operations required to transform the list into a non-decreasing sequence. The function prints the result for each test case.

