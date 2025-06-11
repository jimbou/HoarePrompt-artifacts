#State of the program right berfore the function call: stdin contains multiple inputs: the first line contains an integer (number of test cases), then for each test case, the first line contains two integers (length of the array and number of queries), the second line contains a list of integers (array c), and then for each query, a line contains two integers (left and right borders of the subarray). All integers are positive and the sum of the lengths of the arrays and the number of queries over all test cases does not exceed 3 * 10^5.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: b is a list of n+1 positive integers where each element at index i (1 <= i <= n) is the sum of the number of occurrences of 1 and twice the number of occurrences of any other number in the subarray a[1..i].
    a = list(accumulate(a))
    print(*a)
    #This is printed: the cumulative sums of the elements in the original list a
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The loop will print 'YES' or 'NO' for each iteration, depending on the condition a[y] - a[x - 1] < b[y] - b[x - 1] or x == y. The state of the variables a and b remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts multiple test cases, each consisting of an array and queries on that array. For each test case, it calculates cumulative sums of the array elements and then answers queries by comparing the cumulative sum of a subarray with a calculated value. The function prints 'YES' or 'NO' for each query, depending on the comparison result. The function does not modify the input array or queries, and its output is a series of 'YES' or 'NO' responses, one for each query.

