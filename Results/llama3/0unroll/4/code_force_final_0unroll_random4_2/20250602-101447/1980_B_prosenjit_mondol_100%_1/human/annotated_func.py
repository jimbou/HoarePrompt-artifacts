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
        
    #State: The output state will be a series of 'YES', 'NO', or 'MAYBE' printed to the console, each corresponding to a test case. The number of lines printed will be equal to the value of t in the initial state.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers (n, f, k) and a list of n integers. It then determines whether the f-th integer in the sorted list is greater than, less than, or equal to the k-th integer in the sorted list. Based on this comparison, it prints 'YES', 'NO', or 'MAYBE' to the console for each test case, indicating whether the f-th integer is greater than, less than, or equal to the k-th integer, respectively. If the f-th integer is equal to the k-th integer, it prints 'YES' if the k-th integer is the largest integer in the list, and 'MAYBE' otherwise.

