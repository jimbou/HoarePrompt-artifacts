#State of the program right berfore the function call: stdin contains one input: an integer t (1 <= t <= 10^4), followed by t lines, each containing two integers n and k (2 <= k <= n <= 2 * 10^5), where k is even.
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
        
    #State: The output state will be a series of t lines, each containing a sequence of numbers from 1 to n, where the sequence is constructed by alternating between incrementing and decrementing indices into the array [1, 2, ..., n], starting with incrementing. The sequence will have a length of n.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then generates a sequence of numbers from 1 to n by alternating between incrementing and decrementing indices into the array [1, 2, ..., n], starting with incrementing. The generated sequence is then printed to the console. The function repeats this process for each test case.

