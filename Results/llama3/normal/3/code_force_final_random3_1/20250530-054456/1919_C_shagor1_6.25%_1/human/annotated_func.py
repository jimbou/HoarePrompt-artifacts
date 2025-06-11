#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: n is an integer equal to the first input, inp is an empty list, stdin contains no test cases, _ is the number of test cases, x is the smallest element in the original inp list, y is the second smallest element in the original inp list, ans is the number of elements in the original inp list minus the number of unique elements in the original inp list, a is the last element in the original inp list, and the number of duplicate elements in the original inp list which is ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds the number of duplicate elements in the list by tracking the smallest and second smallest elements encountered so far. The function prints the count of duplicate elements for each test case.

