#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two integers n and k, where 2 <= k <= n <= 2 * 10^5 and k is even.
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
        
    #State: The output state is a sequence of numbers where each number is either 1 more or 1 less than the previous number, starting from 1 and ending at n. The sequence alternates between incrementing and decrementing by 1, with the first number being 1. For example, if n = 5, the output would be 1, 2, 3, 4, 5. If n = 6, the output would be 1, 2, 3, 4, 5, 6.

#Overall this is what the function does:Generates a sequence of numbers where each number is either 1 more or 1 less than the previous number, starting from 1 and ending at n, alternating between incrementing and decrementing by 1, and prints the sequence for multiple test cases.

