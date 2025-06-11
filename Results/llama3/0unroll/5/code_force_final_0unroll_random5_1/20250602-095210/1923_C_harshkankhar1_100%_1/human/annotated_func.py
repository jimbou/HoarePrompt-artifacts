#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case contains two integers n and q (1 <= n, q <= 3 * 10^5), followed by n integers c_1, c_2, ..., c_n (1 <= c_i <= 10^9), followed by q lines, each containing two integers l_i and r_i (1 <= l_i <= r_i <= n).
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: The list b contains the cumulative sum of the number of times each element in list a is greater than 1, starting from the second element (index 1) up to the nth element (index n). The first element of list b (index 0) remains 0.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The loop will execute q times, and in each iteration, it will print 'YES' or 'NO' based on the condition a[y] - a[x - 1] < b[y] - b[x - 1] or x == y. The values of a and b will remain unchanged as they are not modified within the loop. The loop will not have any effect on the initial state of a and b.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints 'YES' or 'NO' for each query based on the condition a[y] - a[x - 1] < b[y] - b[x - 1] or x == y. It does not modify the input values and does not have any side effects beyond printing the results. The function's purpose is to determine whether a certain condition is met for each query and provide a corresponding output.

