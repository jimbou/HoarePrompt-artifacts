#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. Each of the following t lines contains two integers n and k (2 <= k <= n <= 2 * 10^5), where k is even.
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
        
    #State: n is an integer greater than or equal to 1, k is an integer equal to the second input integer, array is a list of integers from 1 to n, stdin contains no lines of input, i is an integer equal to n, answer is a list containing 1 and the last element of array if n is odd, or 1 and the first element of array if n is even, and a is a list containing 1 and -n+1 if n is odd, or a list containing n and -1 if n is even, and the answer is printed which is either [1, n] if n is odd or [1, 1] if n is even.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains two integers n and k. It then generates a list of integers from 1 to n, constructs a new list by alternating between the first and last elements of the original list, and prints this new list. The function repeats this process for each test case.

