#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers t, f, and k (1 <= t, f, k <= 100). The second line contains t integers a_i (1 <= a_i <= 100).
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
        
    #State: The output state after the loop executes all the iterations is a series of 'YES', 'NO', or 'MAYBE' for each test case, indicating whether the kth largest number is greater than, less than, or equal to the number at the fth position in the sorted list of numbers.

#Overall this is what the function does:This function determines whether the kth largest number in a list of numbers is greater than, less than, or equal to the number at the fth position in the sorted list. It takes multiple test cases as input, where each test case consists of three integers (t, f, k) and a list of t integers. For each test case, it outputs 'YES' if the kth largest number is less than the number at the fth position, 'NO' if it's greater, and 'MAYBE' if they are equal and the kth largest number is not the largest number in the list.

