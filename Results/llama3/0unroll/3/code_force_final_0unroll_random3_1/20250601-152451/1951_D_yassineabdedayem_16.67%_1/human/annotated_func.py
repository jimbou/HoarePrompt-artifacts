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
        
    #State: The loop will print either 'YES' or 'NO' for each test case, followed by the length of the list of numbers and the list of numbers itself if 'YES' is printed. The value of `t` remains unchanged, and the contents of `stdin` are consumed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two positive integers n and k. It then attempts to find a sequence of numbers that can be subtracted from n such that the remaining value is 0 and the sum of the sequence is k. If such a sequence is found, it prints 'YES' followed by the length of the sequence and the sequence itself. If no such sequence is found, it prints 'NO'. The function processes multiple test cases and prints the result for each case.

