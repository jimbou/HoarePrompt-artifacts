#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers t, f, and k (1 <= t, f, k <= 100). The second line contains t integers a_i (1 <= a_i <= 100).
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
            print('YES' if k == n - 1 or a[k - 1] < x else 'MAYBE')
        
    #State: n is an integer greater than or equal to 0, f is an integer greater than or equal to 0, k is an integer greater than or equal to 0, a is a sorted list of integers in descending order, x is an integer equal to the value of the element at index f in the list a, _ is equal to the number of test cases, stdin is empty. If a[k] is greater than x, 'NO' is printed. If a[k] is less than or equal to x, 'YES' is printed if k is equal to n - 1 or the element at index k - 1 in the list a is less than x; otherwise, 'MAYBE' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of three integers (t, f, k) and a list of t integers. It sorts the list in descending order, compares the kth element with the element at index f, and prints 'NO' if the kth element is greater, 'YES' if the kth element is less than or equal to the element at index f and either k is the last index or the element before the kth is less than the element at index f, and 'MAYBE' otherwise. The function continues this process until all test cases have been processed, leaving the standard input empty.

