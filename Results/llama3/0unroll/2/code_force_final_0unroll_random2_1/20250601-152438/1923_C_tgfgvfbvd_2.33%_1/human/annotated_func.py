#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then a space-separated list of integers, and then multiple lines each containing two integers. The first integer is the number of test cases. The first integer of each test case is the length of the list of integers, the second integer is the number of queries. The list of integers contains positive integers. The queries contain two integers each, the first integer is the start index of the subarray and the second integer is the end index of the subarray. The start index and end index are 1-indexed. The number of queries does not exceed 3 * 10^5. The length of the list of integers does not exceed 3 * 10^5. The sum of the length of the list of integers over all test cases does not exceed 3 * 10^5. The sum of the number of queries over all test cases does not exceed 3 * 10^5.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: The output state is a series of 'YES' or 'NO' for each query in each test case, indicating whether the sum of the subarray from index a to b is greater than or equal to twice the length of the subarray. The number of 'YES' or 'NO' outputs is equal to the total number of queries across all test cases.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains a list of integers and multiple queries. For each query, it determines whether the sum of the subarray from the given start index to the end index is greater than or equal to twice the length of the subarray, and outputs 'YES' if true and 'NO' otherwise. The function iterates through all test cases and queries, providing a series of 'YES' or 'NO' outputs indicating the result of each query.

