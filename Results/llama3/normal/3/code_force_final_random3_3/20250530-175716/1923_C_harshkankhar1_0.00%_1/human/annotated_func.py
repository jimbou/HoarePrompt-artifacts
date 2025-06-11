#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 10^4), then for each test case, it contains two integers n and q (1 <= n, q <= 3 * 10^5), followed by n integers c_1, c_2, ..., c_n (1 <= c_i <= 10^9), and then q lines each containing two integers l_i and r_i (1 <= l_i <= r_i <= n).
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: a is a list of n+1 integers where the first element is 0 and the remaining elements are the input integers c_1, c_2, ..., c_n, b is a list of n+1 integers where the first element is 0 and the remaining elements are the cumulative sums of 1 if c_i > 1 else 2 for i from 1 to n, n is an integer between 1 and 3 * 10^5, q is an integer between 1 and 3 * 10^5, stdin contains t-1 test cases, i is n.
    a = list(accumulate(a))
    print(*a)
    #This is printed: [0, cumulative sum of c_1, cumulative sum of c_1 + c_2, ..., cumulative sum of c_1 + c_2 + ... + c_n]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: a is a list of n+1 integers where the first element is 0 and the remaining elements are the cumulative sums of the input integers c_1, c_2, ..., c_n, b is a list of n+1 integers where the first element is 0 and the remaining elements are the cumulative sums of 1 if c_i > 1 else 2 for i from 1 to n, n is an integer between 1 and 3 * 10^5, q is 0, stdin contains t-q test cases, i is n, the elements of the list a have been printed, and either 'YES' or 'NO' has been printed q times depending on the values of x and y.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts no parameters and returns no values. The function reads an integer t, then for each test case, it reads two integers n and q, followed by n integers c_1, c_2, ..., c_n, and then q lines each containing two integers l_i and r_i. It calculates the cumulative sums of the input integers and the cumulative sums of 1 if c_i > 1 else 2, and prints the cumulative sums of the input integers. Then, for each query, it prints 'YES' if the cumulative sum of the input integers from l_i to r_i is greater than or equal to the cumulative sum of 1 if c_i > 1 else 2 from l_i to r_i, and 'NO' otherwise.

