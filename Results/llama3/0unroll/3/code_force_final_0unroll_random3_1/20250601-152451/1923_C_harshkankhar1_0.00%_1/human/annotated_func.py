#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three inputs: first an integer, then two space-separated integers, then a space-separated list of integers, and then multiple lines each containing two space-separated integers. The first integer is the number of test cases. The first integer of the second line of each test case is the length of the list of integers. The second integer of the second line of each test case is the number of queries. The list of integers contains only positive integers. The queries are pairs of integers such that 1 <= l <= r <= n.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: The value of b[i] is updated to be the sum of the previous value of b[i-1] and 1 if a[i] is greater than 1, or 2 if a[i] is 1, for all i from 1 to n. The values of n, q, and a remain unchanged.
    a = list(accumulate(a))
    print(*a)
    #This is printed: [cumulative sum of a up to index 0], [cumulative sum of a up to index 1], ..., [cumulative sum of a up to index n-1]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: The value of `a` is updated to be the cumulative sum of its previous values, `n`, `q`, and `b` remain unchanged, and the value of b[i] is the sum of the previous value of b[i-1] and 1 if the cumulative sum of a up to index i is greater than 1, or 2 if the cumulative sum of a up to index i is 1, for all i from 1 to n, and the cumulative sum of a up to index i is being printed for all i from 0 to n.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer, two space-separated integers, a list of integers, and multiple lines of queries. It calculates the cumulative sum of the list of integers and prints it. Then, for each query, it checks if the cumulative sum of the list up to the second index is greater than or equal to the sum of the previous values plus 1 (or 2 if the cumulative sum is 1) and prints 'YES' if true, 'NO' otherwise. The function does not modify the input values except for the cumulative sum calculation.

