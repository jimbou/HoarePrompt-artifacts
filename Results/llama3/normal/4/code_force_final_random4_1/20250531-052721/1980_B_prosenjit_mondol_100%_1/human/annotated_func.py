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
        
    #State: n is an integer, f is an integer, k is an integer, a is a sorted list of integers in descending order, x is an integer equal to the value of a at index f after sorting, _ is equal to the number of test cases, stdin is empty. If a[k] is greater than x, 'NO' is printed. If a[k] is less than x, 'YES' is printed. If a[k] is not less than x and k is not the last index of a, either 'YES' or 'MAYBE' is printed based on the condition a[k + 1] < x.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: t (the number of elements), f (an index), and k (another index). The second line contains t integers. The function sorts these integers in descending order, compares the value at index k with the value at index f, and prints 'YES', 'NO', or 'MAYBE' based on this comparison. If the value at index k is greater than the value at index f, it prints 'NO'. If the value at index k is less than the value at index f, it prints 'YES'. If the values are equal and k is not the last index, it prints 'YES' if the next value is less than the value at index f, otherwise it prints 'MAYBE'. The function processes all test cases and empties the standard input.

