#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers a, b, c (0 <= a, b, c <= 10^9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: n is an integer greater than or equal to 0 and less than or equal to 10^4, a is an integer, b is an integer, c is an integer, i is n, stdin is empty. If (b % 3 != 0 and c < 3) and (b + c) % 3 != 0, then -1 is printed n times. Otherwise, if (b + c) % 3 != 0, then k is an integer equal to n plus the sum of n instances of a plus one-third of the sum of b and c and k is printed n times. Otherwise, k is an integer equal to n plus the sum of n instances of a plus one-third of the sum of b and c and k is printed n times.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains three integers a, b, and c. It then calculates and prints a value k for each set of a, b, and c, based on certain conditions. If (b % 3 != 0 and c < 3) and (b + c) % 3 != 0, it prints -1. Otherwise, it calculates k as the sum of a, plus one-third of the sum of b and c, and prints this value. The function repeats this process t times, after which stdin is empty.

