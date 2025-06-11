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
            print('YES' if k == n - 1 or a[k - 1] < x else 'MAYBE')
        
    #State: n is an integer, f is an integer minus one, k is an integer minus one, a is a sorted list of integers in descending order, x is an integer equal to the value of a at index f, _ is equal to the initial value of t, stdin is empty. If a[k] is greater than x, 'NO' is printed. If a[k] is less than x, 'YES' is printed. If a[k] is equal to x, 'YES' is printed if k is equal to n minus one or the value of a at index k minus one is less than x, otherwise 'MAYBE' is printed.

#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and prints the result for each case. It takes no parameters and returns no value. For each test case, it reads three integers (n, f, k) and a list of n integers, sorts the list in descending order, and compares the value at index k with the value at index f. Based on the comparison, it prints 'NO', 'YES', or 'MAYBE' to indicate whether the value at index k is greater than, less than, or equal to the value at index f, respectively. If the values are equal, it also checks if k is equal to n-1 or the value at index k-1 is less than the value at index f to determine whether to print 'YES' or 'MAYBE'.

