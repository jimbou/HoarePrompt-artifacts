#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two integers n and q, and then a list of n integers. The integer is a positive integer and represents the number of test cases. n and q are positive integers. The list of integers contains positive integers.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: The number of test cases has been reduced by 1, n is a positive integer, q is a positive integer, a is a list of n+1 positive integers where the first element is 0 and the rest are the input integers, b is a list of n+1 positive integers where the first element is 0 and the rest are the cumulative sums of 1's and 2's based on the values in list a.
    a = list(accumulate(a))
    print(*a)
    #This is printed: The cumulative sums of all elements up to each index in the original list a
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: The number of test cases has been reduced by 1, `n` is a positive integer, `q` is 0, `a` is a list of `n+1` positive integers where each element is the cumulative sum of all elements up to that index in the original list, `b` is a list of `n+1` positive integers where the first element is 0 and the rest are the cumulative sums of 1's and 2's based on the values in the original list `a`, and the list `a` is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads an integer n, an integer q, and a list of n integers. It calculates the cumulative sums of the input list and another list where each element is either 1 or 2 based on the corresponding element in the input list. It then prints the cumulative sums of the input list. After that, it reads q queries, each consisting of two integers x and y, and for each query, it checks if the cumulative sum of the input list from index x to y is less than the cumulative sum of the other list from index x to y. If so, it prints 'NO', otherwise, it prints 'YES'. The function repeats this process until all test cases are processed.

