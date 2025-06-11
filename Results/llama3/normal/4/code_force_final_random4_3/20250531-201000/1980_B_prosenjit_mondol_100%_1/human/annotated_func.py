#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, f, and k (1 <= f, k <= n <= 100). The second line contains n integers a_i (1 <= a_i <= 100).
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: n is an integer, f is an integer, k is an integer, a is a sorted list of integers in descending order, x is the integer at index f in the list a, stdin is empty. If a[k] is greater than x, 'NO' is printed. If a[k] is less than x, 'YES' is printed. If a[k] is equal to x, if k is equal to n - 1 or the integer at index k + 1 in the list a is less than the integer at index f in the list a, 'YES' is printed; otherwise, 'MAYBE' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, f, k) and a list of n integers. It then determines whether the integer at index f in the sorted list is greater than, less than, or equal to the integer at index k. Based on this comparison, it prints 'YES', 'NO', or 'MAYBE' to indicate whether the integer at index f is greater than or equal to the integer at index k, or if it's uncertain. The function processes multiple test cases and prints the result for each case.

