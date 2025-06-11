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
        
    #State: n is an integer greater than or equal to 0, f is an integer, k is an integer, a is a sorted list of integers in descending order, x is an integer equal to the value of a at index f, _ is equal to the initial value of t. If a[k] is greater than x, 'NO' is printed. If a[k] is less than x, 'YES' is printed. If a[k] is not less than x, then if k is equal to n - 1 or the element at index k + 1 in the list a is less than x, 'YES' is printed. Otherwise, 'MAYBE' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the result for each case. It takes no parameters and returns no value. For each test case, it reads three integers (n, f, k) and a list of n integers, sorts the list in descending order, and compares the value at index f with the value at index k. Based on the comparison, it prints 'NO' if the value at index k is greater, 'YES' if the value at index k is less, and 'YES' or 'MAYBE' if the values are equal, depending on whether k is the last index or the next value in the list is less than the value at index f.

