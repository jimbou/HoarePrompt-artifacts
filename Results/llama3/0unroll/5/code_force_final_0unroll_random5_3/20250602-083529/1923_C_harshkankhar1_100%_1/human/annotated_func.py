#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a space-separated list of two integers, and then a list of space-separated integers. Each test case is followed by a number of queries, each query being a space-separated list of two integers.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: The value of b[i] is updated for each i from 1 to n, where b[i] is the sum of b[i-1] and 1 if a[i] is greater than 1, otherwise 2. The values of n, q, a, and stdin remain unchanged.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The loop has executed q times, and for each iteration, it has printed either 'YES' or 'NO' based on the condition a[y] - a[x - 1] < b[y] - b[x - 1] or x == y. The values of n, q, b, and stdin remain unchanged. The value of a[i] is still the sum of all elements in a from index 0 to i, but the loop has not modified the array a.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads an integer n, a list of n+1 integers, and a list of q queries. It then calculates a cumulative sum of the input list and a second list b, where each element b[i] is the sum of b[i-1] and 1 if the corresponding element in the input list is greater than 1, otherwise 2. The function then answers q queries, each consisting of two integers x and y, by printing 'YES' if the sum of elements in the input list from x to y is greater than or equal to the sum of elements in list b from x to y, and 'NO' otherwise.

