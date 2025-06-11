#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 1000) followed by t lines, each containing two positive integers n and k (1 ≤ n, k ≤ 10^18).
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        rep = 0
        
        number = 0
        
        tab = []
        
        while n != 0 and k > 0 and rep < 60 and n >= k:
            Min, Max = min(n // k, k), max(int(n / k), k)
            if Max == k and n * Min <= k:
                number = Min
                k = k - Max
            else:
                number = Max
                k = k - Min
            tab.append(str(number))
            n -= Min * Max
            rep += 1
        
        if k == 0:
            print('YES')
            print(len(tab))
            for i in tab:
                print(i, end=' ')
        else:
            print('NO')
        
    #State: Output State: The output state will contain 't' number of lines. Each line will either contain 'NO' or 'YES' followed by the length of the list 'tab' and the elements of 'tab' separated by a space. The value of 't' remains unchanged as it is not affected by the loop head and body.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts a variable number of test cases, each consisting of two positive integers, and attempts to find a sequence of numbers that satisfy a specific condition. If a valid sequence is found, it prints 'YES' followed by the length of the sequence and the sequence itself. If no valid sequence is found, it prints 'NO'. The function does not return any value and does not modify any external state, only printing output to standard output.

