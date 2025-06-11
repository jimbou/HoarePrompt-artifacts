#State of the program right berfore the function call: stdin contains one input: an integer t (1 <= t <= 10^4) followed by t lines each containing two integers n and k (2 <= k <= n <= 2 * 10^5), where k is even.
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
        
    #State: The output state will contain t lines, each containing a sequence of n integers. The sequence is constructed by alternating between the first and last elements of the array, moving towards the center. The first element of the sequence is always 1. For example, if n = 5 and k = 4, the output will be: 1 5 2 4 3.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts an integer t (1 <= t <= 10^4) followed by t lines each containing two integers n and k (2 <= k <= n <= 2 * 10^5), where k is even. The function constructs a sequence of n integers by alternating between the first and last elements of an array, moving towards the center, and prints this sequence for each input line. The first element of the sequence is always 1. The function returns no value but prints t lines of output, each containing a sequence of n integers.

