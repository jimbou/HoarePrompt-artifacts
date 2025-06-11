#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains three space-separated integers a, b, c (0 <= a, b, c <= 10^9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: n is greater than or equal to 0, i is n, a, b, c are undefined, stdin contains no input. If n is 0, no output is printed. If n is greater than 0, the loop executes n times, and for each iteration, if b is not divisible by 3 and the sum of b modulo 3 and c is less than 3, then -1 is printed. Otherwise, k is updated to be the sum of its initial value, a, and the integer division of b plus c by 3, and if the remainder of the division of b plus c by 3 is not 0, k is increased by 1, and the value of k is printed.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains three space-separated integers a, b, and c. It then processes each set of a, b, and c, and prints a value based on the divisibility of b and the sum of b and c. If b is not divisible by 3 and the sum of b modulo 3 and c is less than 3, it prints -1. Otherwise, it calculates a value k as the sum of a, the integer division of b plus c by 3, and an additional 1 if the remainder of the division is not 0, and prints this value. The function repeats this process t times, or not at all if t is 0.

