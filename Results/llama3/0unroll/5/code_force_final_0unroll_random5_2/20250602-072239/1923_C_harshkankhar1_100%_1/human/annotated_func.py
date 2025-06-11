#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a space-separated list of integers, and then multiple lines of two integers. The first integer is the number of test cases. The second integer is the length of the array and the number of queries. The list of integers is the array c. The lines of two integers are the borders of the subarray.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: The list b now contains the cumulative sum of 1s and 2s, where 1 is added if the corresponding element in list a is greater than 1, and 2 is added otherwise. The rest of the variables remain unchanged.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: The list a now contains the cumulative sum of its original elements, where each element is the sum of all elements up to that point in the original list. The rest of the variables remain unchanged.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads an integer array and a number of queries. It then calculates the cumulative sum of the array and a modified cumulative sum where each element is either 1 or 2 based on the corresponding element in the original array. The function then answers queries by comparing the cumulative sums of subarrays. If the cumulative sum of the original subarray is less than the modified cumulative sum, it prints 'NO', otherwise, it prints 'YES'. The function repeats this process for all test cases.

