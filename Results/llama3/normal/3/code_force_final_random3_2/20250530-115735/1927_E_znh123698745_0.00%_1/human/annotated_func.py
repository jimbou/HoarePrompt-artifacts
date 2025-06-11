#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of two space-separated integers: n and k, where 2 <= k <= n <= 2 * 10^5 and k is even.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        array = list(range(1, n + 1))
        
        answer = [1]
        
        a = [1, -1]
        
        for i in range(1, n):
            if (-1) ** i == -1:
                answer.append(array[a[-1]])
                a[-1] -= 1
            else:
                answer.append(array[a[0]])
                a[0] += 1
        
        print(*answer)
        
    #State: n is an integer greater than 0, k is an integer, array is a list of integers from 1 to n, answer is a list containing the integers from 1 to n in the order of 1, n, 2, n-1, 3, n-2, ..., n/2, n/2+1 if n is even or (n+1)/2, (n+1)/2 if n is odd, a is a list containing the integers n/2+1 and -n/2 if n is even or (n+1)/2 and -(n+1)/2 if n is odd, _ is the number of test cases, stdin is empty, and i is equal to n, and the answer list containing the integers from 1 to n in the order of 1, n, 2, n-1, 3, n-2, ..., n/2, n/2+1 if n is even or (n+1)/2, (n+1)/2 if n is odd is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers: n and k. It generates a list of integers from 1 to n, then rearranges this list in a specific order (1, n, 2, n-1, 3, n-2, ..., n/2, n/2+1 if n is even or (n+1)/2, (n+1)/2 if n is odd) and prints this rearranged list. The function repeats this process for each test case, until all input has been processed and standard input is empty.

