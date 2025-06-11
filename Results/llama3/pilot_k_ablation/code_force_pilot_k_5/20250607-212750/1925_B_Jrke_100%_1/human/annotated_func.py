#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 ≤ t ≤ 10^3), then t pairs of integers x and n (1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: t is an integer greater than or equal to 0, x is an integer greater than or equal to 0, n is an integer, k is an integer, ans is the maximum divisor of x that is less than or equal to k, l is a list containing the value of ans, i is an integer equal to int(x

#Overall this is what the function does:This function reads a series of input pairs from standard input, where each pair consists of an integer x and n. For each pair, it calculates the maximum divisor of x that is less than or equal to x divided by n, and prints this value. The function processes multiple pairs of inputs, as specified by an initial integer t, which indicates the number of pairs to follow.

