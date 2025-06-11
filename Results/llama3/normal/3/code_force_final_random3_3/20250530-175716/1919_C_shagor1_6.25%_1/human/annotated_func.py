#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2*10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n).
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: _ is the number of test cases in the input, stdin is empty, n is an integer equal to the input value, inp is an empty list, x is the smallest integer in the list that is less than or equal to n + 1, y is the second smallest integer in the list that is less than or equal to n + 1, ans is the number of integers in the list that are greater than the second smallest integer in the list that is less than or equal to n + 1, and a is undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It then finds the smallest and second smallest integers in the list that are less than or equal to n + 1, and counts the number of integers in the list that are greater than the second smallest integer. The function prints the count for each test case, effectively processing and analyzing the input data.

