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
        
    #State: The output state will be a series of 'YES', 'NO', or 'MAYBE' printed to the console, each corresponding to the result of the comparison for each test case. The number of outputs will be equal to the number of test cases t.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers (n, f, k) and a list of n integers. It then compares the f-th integer in the list to the k-th largest integer in the sorted list. If the k-th largest integer is greater than the f-th integer, it prints 'NO'. If the k-th largest integer is less than the f-th integer, it prints 'YES'. If the k-th largest integer is equal to the f-th integer, it prints 'YES' if k is the last index or the (k-1)-th largest integer is less than the f-th integer, otherwise it prints 'MAYBE'. The function repeats this process for each test case and prints the results to the console.

