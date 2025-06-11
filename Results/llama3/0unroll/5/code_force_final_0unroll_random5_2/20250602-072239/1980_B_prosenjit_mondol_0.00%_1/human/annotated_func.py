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
        
    #State: The output state is a series of 'YES', 'NO', or 'MAYBE' printed for each test case, indicating whether the kth largest number in the sorted list is greater than, less than, or equal to the number at index f in the original list.

#Overall this is what the function does:Determines whether the kth largest number in a sorted list is greater than, less than, or equal to the number at a specified index f in the original list, and prints 'YES', 'NO', or 'MAYBE' accordingly for each test case.

