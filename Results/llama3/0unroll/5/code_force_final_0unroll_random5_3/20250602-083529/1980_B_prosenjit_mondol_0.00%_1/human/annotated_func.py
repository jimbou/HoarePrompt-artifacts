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
        
    #State: The output state after the loop executes all the iterations is a series of 'YES', 'NO', or 'MAYBE' printed to the console, each corresponding to whether the kth largest element in the sorted array is greater than, less than, or equal to the element at index f. The number of outputs is equal to the number of test cases t.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an array of integers and two indices. It then determines whether the kth largest element in the sorted array is greater than, less than, or equal to the element at the specified index, printing 'YES', 'NO', or 'MAYBE' to the console for each test case, respectively.

